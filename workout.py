import os
from flask import Flask, render_template, url_for, flash, redirect, request, session
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

        user = mongo.db.users.find_one({"username": form.username.data.lower()})

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
    Allows user to login with existing account.
    """

    if current_user.is_authenticated:

        flash("You are already logged in.", 'error')
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():

        user = mongo.db.users.find_one({"username": form.username.data.lower()})

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
    logout_user()
    session.clear()
    flash('You have successfully logged out.', 'normal')
    return redirect(url_for('login'))

# Muscle groups

@app.route('/muscle_groups')
def muscle_groups():
    """
    Allows user to view the muscle groups.
    """
    return render_template('groups.html')


# Push Exercises

@app.route('/push')
def push():
    """
    Displays all push exercises
    """
    return render_template('push.html', exercises=mongo.db.exercises.find({
                                                "category_name": "Push"}))


# Pull Exercises

@app.route('/pull')
def pull():
    """
    Displays all pull exercises
    """
    return render_template('pull.html', exercises=mongo.db.exercises.find({
                                                "category_name": "Pull"}))


# Legs Exercises

@app.route('/legs')
def legs():
    """
    Displays all legs exercises
    """
    return render_template('legs.html', exercises=mongo.db.exercises.find({
                                                "category_name": "Legs"}))


# Core Exercises

@app.route('/core')
def core():
    """
    Displays all core exercises
    """
    return render_template('core.html', exercises=mongo.db.exercises.find({
                                                "category_name": "Core"}))

# My exercises

    """
    Allows user to see all his/her added exercises.
    """
"""
@app.route('/my_exercises/<username>')
@login_required
def my_exercises(username):
    

    user = mongo.db.users.find_one({'username': username})

    user_exercises = mongo.db.exercises.find({'added_by': username}).sort([("_id", -1)])

    return render_template('my_exercises.html', user=user, exercises=user_exercises, title='My Exercises')
"""

@app.route('/my_exercises')
@login_required
def my_exercises():
    username = current_user.username
    user = mongo.db.users.find_one({'username': username})

    user_exercises = mongo.db.exercises.find({'added_by': username}).sort([("_id", -1)])
    return render_template('my_exercises.html', user=user, exercises=user_exercises, title='My Exercises')

# Add Exercise

@app.route('/add_exercise')
@login_required
def add_exercise():
    user = session['username']
    form = ExerciseForm()

    return render_template('add_exercise.html', user=user, title='Add Exercise', form=form)

# Insert Exercise

@app.route('/insert_exercise', methods=['POST'])
@login_required
def insert_exercise():

    exercises = mongo.db.exercises
    username = current_user.username

    category_name = request.form['category_name']
    exercise_name = request.form['exercise_name']

    existing_exercise = mongo.db.exercises.count_documents({'$and':
        [{'category_name': category_name},
        {'exercise_name': exercise_name}]
    })

    if existing_exercise == 0:

        exercises.insert_one({
            'category_name': request.form['category_name'],
            'exercise_name': request.form['exercise_name'],
            'muscles': request.form['muscles'],
            'exercise_difficulty': request.form['exercise_difficulty'],
            'equipment': request.form['equipment'],
            'exercise_instructions': request.form['exercise_instructions'],
            'added_by': username
        })

        flash('Your exercise has been successfully added.', 'normal')

    else:
        flash('An exercise with the same name already exists.', 'error')

    return redirect(url_for('my_exercises'))

# Set up of IP address and PORT number

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
