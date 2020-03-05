import os
from flask import Flask, render_template, url_for, flash, redirect, request, session, jsonify
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import LoginForm, RegistrationForm, ExerciseForm
from werkzeug.security import generate_password_hash, check_password_hash
from user import User
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

login = LoginManager(app)
login.login_view = 'login'


# Index/home

@app.route('/')
@app.route('/index')
def index():
    """
    Home page - landing page
    """
    return render_template('index.html')


# Register new account

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Enables user to register a new account.
    """

    if current_user.is_authenticated:

        flash("You are already logged in.", 'error')
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():

        user = mongo.db.users.find_one({
            "username": form.username.data.lower()})

        if user is None:
            password = generate_password_hash(request.form['password'])
            mongo.db.users.insert_one({
                                'username': request.form['username'].lower(),
                                'password': password
            })
            flash('You have successfully registered as a new user! You can now log into your account', 'normal')
            return redirect(url_for('login'))

        else:
            flash('This username is already in use. Please try a different one.', 'error')

    return render_template('register.html', title='Register', form=form)


# User Loader Function

@login.user_loader
def load_user(username):

    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None

    return User(u['username'])


# Login with existing account

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Allows user to login with existing account. This view checks
    if username exists in the database and if the password is correct.
    """

    if current_user.is_authenticated:

        flash("You are already logged in.", 'error')
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():

        user = mongo.db.users.find_one({
            "username": form.username.data.lower()})

        if user and User.check_password(user['password'], form.password.data):

            user_info = User(user['username'])
            login_user(user_info)
            session['username'] = request.form['username']
            flash("You have successfully logged in.", 'normal')
            return redirect(url_for('index'))

        elif user is None:

            flash('Username does not exist.', 'error')

        else:

            flash('Wrong password.', 'error')

    return render_template('login.html', title='Login', form=form)


# Logout

@app.route('/logout')
def logout():
    """
    Enables user to log out.
    """

    logout_user()
    session.clear()
    flash('You have successfully logged out.', 'normal')
    return redirect(url_for('login'))


# Muscle groups

@app.route('/muscle_groups')
def muscle_groups():
    '''
    Allows user to view the four muscle groups.
    '''

    return render_template('groups.html')


# Categories

@app.route('/<category>')
def get_category(category):
    '''
    This view will take in a category name, and return
    all of the exercises within that category.
    The exercises will be sorted with the most liked
    exercises on the top.
    '''

    exercises = mongo.db.exercises.find({
            "category_name": category.title()
        }).sort([("like_total", -1)])

    return render_template("category.html",
                           category=category,
                           exercises=exercises)


# My exercises
# Allows user to see all his/her added exercises.

@app.route('/my_exercises')
@login_required
def my_exercises():
    '''
    This view will return all of the exercises that
    a user has liked and added to the database.
    '''

    username = current_user.username
    user = mongo.db.users.find_one({
        'username': username})
    added_exercises = mongo.db.exercises.find({
        'added_by': username}).sort([("category_name", 1)])
    liked_exercises = mongo.db.exercises.find({
        'like': {
            '$elemMatch': {
                "username": username
            }
        }
    }).sort([("category_name", 1)])

    return render_template('my_exercises.html',
                           user=user,
                           added_exercises=added_exercises,
                           liked_exercises=liked_exercises,
                           title='My Exercises')


# Delete Account

@app.route('/delete_account/<user_id>')
@login_required
def delete_account(user_id):
    '''
    This view will take in a user_id to then deduct the total
    counts of the like and dislike values for the exercises a
    user voted for, then the username is being removed from the
    arrays of the like / dislike variables. Additionally all
    exercises a user has added are removed and finally the user
    itself is removed from the database.
    '''

    username = current_user.username

    # first remove vote from total likes/dislikes for all
    # exercises the user has voted
    mongo.db.exercises.update_many(
        {'like': {'username': username}},
        {'$inc': {'like_total': -1}}
    )

    mongo.db.exercises.update_many(
        {'dislike': {'username': username}},
        {'$inc': {'dislike_total': -1}}
    )

    # then remove username from all exercises that user has liked/disliked
    mongo.db.exercises.update_many(
        {'like': {'username': username}},
        {'$pull': {'like': {'username': username}}}
    )

    mongo.db.exercises.update_many(
        {'dislike': {'username': username}},
        {'$pull': {'dislike': {'username': username}}}
    )

    # remove all exercises the user has added
    mongo.db.exercises.remove({'added_by': username})

    # remove the user
    mongo.db.users.remove({'_id': ObjectId(user_id)})

    session.clear()

    return redirect(url_for('index'))


# Add Exercise

@app.route('/<category>/add_exercise', methods=['GET', 'POST'])
@login_required
def add_exercise(category):
    '''
    This view will take in a category and renders the exercise
    form.
    '''

    user = session['username']
    form = ExerciseForm()

    return render_template('add_exercise.html',
                           user=user, category=category,
                           form=form, title='Add Exercise')


# Insert Exercise

@app.route('/<category>/insert_exercise', methods=['POST'])
@login_required
def insert_exercise(category):
    '''
    This view will take in a category and inserts an exercise
    to the database once the user clicks on the submit button.
    '''

    exercises = mongo.db.exercises
    username = current_user.username

    category_name = request.form['category_name']
    exercise_name = request.form['exercise_name']

    existing_exercise = mongo.db.exercises.count_documents({'$and': [{
        'category_name': category_name}, {
        'exercise_name': exercise_name}
        ]
    })

    if existing_exercise == 0:

        exercises.insert_one({
            'category_name': request.form['category_name'],
            'exercise_name': request.form['exercise_name'],
            'muscles': request.form['muscles'],
            'exercise_difficulty': request.form['exercise_difficulty'],
            'equipment': request.form['equipment'],
            'exercise_instructions': request.form['exercise_instructions'],
            'added_by': username,
            'like': [],
            'dislike': [],
            'like_total': 0,
            'dislike_total': 0
        })

        flash('Your exercise has been successfully added.', 'normal')

    else:
        flash('An exercise with the same name already exists.', 'error')

    return redirect(url_for('get_category', category=category))


# Edit Exercise

@app.route('/<category>/edit_exercise/<exercise_id>', methods=['GET', 'POST'])
@login_required
def edit_exercise(category, exercise_id):
    '''
    This view will take in a category and an exercise_id and
    renders the edit exercise form.
    '''

    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    form = ExerciseForm()

    return render_template('edit_exercise.html',
                           category=category,
                           exercise=the_exercise, form=form)


# Update Exercise

@app.route('/<category>/update_exercise/<exercise_id>', methods=['GET',
                                                                 'POST'])
@login_required
def update_exercise(category, exercise_id):
    '''
    This view will take in a category and an exercise_id and
    updates the information about an exercise, after the user
    has clicked the submit button in the edit form.
    '''

    exercises = mongo.db.exercises

    exercises.update({'_id': ObjectId(exercise_id)}, {'$set': {
        'category_name': request.form.get('category_name'),
        'exercise_name': request.form.get('exercise_name'),
        'muscles': request.form.get('muscles'),
        'exercise_difficulty': request.form.get('exercise_difficulty'),
        'equipment': request.form.get('equipment'),
        'exercise_instructions': request.form.get('exercise_instructions')}
    })

    return redirect(url_for('get_category', category=category))


# Delete Exercise

@app.route('/delete_exercise/<exercise_id>')
@login_required
def delete_exercise(exercise_id):
    '''
    This view will take in an exercise_id and removes
    the exercise from the database.
    '''

    mongo.db.exercises.remove({'_id': ObjectId(exercise_id)})

    return redirect(url_for('my_exercises'))


# Like / Dislike Functionality

'''
Functionality that will add or remove a vote from username arrays
and increase the total voted numbers
'''


def add_vote(vote_type, vote_type_total, exercise_id, username):
    mongo.db.exercises.update({"_id": ObjectId(exercise_id)},
                              {'$push': {vote_type: {'username': username}}})

    mongo.db.exercises.find_one_and_update({'_id': ObjectId(exercise_id)},
                                           {'$inc': {vote_type_total: 1}})


def remove_vote(vote_type, vote_type_total, exercise_id, username):

    mongo.db.exercises.update({"_id": ObjectId(exercise_id)},
                              {'$pull': {vote_type: {'username': username}}})

    mongo.db.exercises.find_one_and_update({'_id': ObjectId(exercise_id)},
                                           {'$inc': {vote_type_total: -1}})


# Like

@app.route('/like/<exercise_id>', methods=['GET', 'POST'])
@login_required
def like(exercise_id):
    '''
    This view takes in an exercise_id and and enables users to
    like an exercise storing the username in the like variable
    and increasing the like_total number by 1
    '''

    username = current_user.username

    # Check if current user has already liked the exercise
    match_count_like = mongo.db.exercises.count_documents({
        '_id': ObjectId(exercise_id),
        'like': {'$elemMatch': {"username": username}},
    })

    # Check if current user has already disliked the exercise
    match_count_dislike = mongo.db.exercises.count_documents({
        '_id': ObjectId(exercise_id),
        'dislike': {'$elemMatch': {"username": username}},
    })

    # If user already liked the exercise then remove his/her like
    if match_count_like > 0:

        remove_vote('like', 'like_total', exercise_id, username)

    # If user already disliked the exercise then remove his/her dislike and add like
    elif match_count_dislike > 0:

        add_vote('like', 'like_total', exercise_id, username)
        remove_vote('dislike', 'dislike_total', exercise_id, username)

    # If user neither liked nor disliked the exercise add like
    else:

        add_vote('like', 'like_total', exercise_id, username)

    return redirect(url_for('my_exercises', exercise_id=exercise_id))


# Disike

@app.route('/dislike/<exercise_id>', methods=['GET', 'POST'])
@login_required
def dislike(exercise_id):
    '''
    This view takes in an exercise_id and and enables users to
    dislike an exercise storing the username in the dislike
    variable and decreasing the dislike_total number by 1
    '''

    username = current_user.username

    # Check if current user has already liked the exercise
    match_count_like = mongo.db.exercises.count_documents({
        '_id': ObjectId(exercise_id),
        'like': {'$elemMatch': {"username": username}},
    })

    # Check if current user has already disliked the exercise
    match_count_dislike = mongo.db.exercises.count_documents({
        '_id': ObjectId(exercise_id),
        'dislike': {'$elemMatch': {"username": username}},
    })

    # If user already disliked the exercise then remove his/her dislike
    if match_count_dislike > 0:

        remove_vote('dislike', 'dislike_total', exercise_id, username)

    # If user already liked the exercise then remove like and add dislike
    elif match_count_like > 0:
        remove_vote('like', 'like_total', exercise_id, username)
        add_vote('dislike', 'dislike_total', exercise_id, username)

    # If user neither liked nor disliked the exercise add dislike
    else:
        add_vote('dislike', 'dislike_total', exercise_id, username)

    return redirect(url_for('muscle_groups', exercise_id=exercise_id))


# Search
# Functionality that enables the user to search for specific exercises

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    '''
    This view enables the user to search for exercises by name,
    affected muscles and exercise difficulty.
    '''

    search_input = request.form.get("search_input")
    search_string = str(search_input)

    mongo.db.exercises.create_index([('exercise_name', 'text'),
                                     ('muscles', 'text'),
                                     ('exercise_difficulty', 'text')])

    # Search results and sort by id
    search_results = mongo.db.exercises.find(
        {"$text": {"$search": search_string}}).sort([("_id", -1)])

    results_count = mongo.db.exercises.count_documents(
        {"$text": {"$search": search_string}})

    if request.method == 'POST':

        # If no search input flash the message
        if search_string == '':

            flash('You have not provided any search input! Please try again or browse through all exercises.', 'error')

            return redirect('/muscle_groups')

        # If no results display info message
        elif results_count == 0:

            flash(f'No matching results found for "{search_input}". Please try a different search or browse through all exercises', 'error')

            return redirect('/muscle_groups')

        # Display search result
        else:

            return render_template('search.html', exercises=search_results)

    return render_template('search.html', exercises=search_results)


# Set up of IP address and PORT number

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
