# Find Your Workout

Stream Three Project - Data Centric Development Milestone - Code Institute

This website will help you get inspiration and ideas for your next workout. You will find different kinds of exercises for each muscle group and will also have to possibility to add your own exercises to the database to share with others.

## Table of Contents

1. [Demo](#demo)
2. [UX](#ux)
3. [Database](#database)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Demo

Check out the deployed website [here](https://find-your-workout.herokuapp.com/).

## UX

To create a sleek look and a homogeneous experience for the user I used the colors black, white and grey consistently throughout the project.

In order to create a easy and intuitive user experience I designed the website in a way where it is simple for the user to use.

### Target Audience

The website targets anyone who is interested in finding out more about not only what exercises to do in order to stay fit but also how to do them and what equipment is needed. More than that, this application also enables users to create own exercises and like existing exercises in order to build up a user page with liked and added exercises.

Therefore this application enables the user to read, add, edit and rate exercises.

### User Stories

As a user I expect/would like/need:

1. to create an account in order to acces the existing exercises.

2. to delete my account if I don't see the need in having it anymore.

3. the option to login/logout in order that only users can see the content.

4. to view the existing exercises to get inspired for my next workout.

5. to have the exercises sorted in different categories in order to look for a specific muscle group.

6. to add my own exercises and share them with other users.

7. to edit the exercises that were added by me.

8. to delete exercises that were added by me.

9. that no other users are able to edit and delete the exercises that I added.

10. to like and dislike exercises.

11. to remove my like or dislike if I change my mind about the exercise.

12. to have all my liked and added exercises summarized in one place for me to access it.

13. to see which exercises are the most favorized ones.

### Wireframes

In the planing process using [Balsamiq](https://balsamiq.cloud/) following [wireframes](https://github.com/alnibo/milestone-project-3-workout/tree/master/wireframes) were created in order to design the layout for this project for mobile, medium and desktop views.

## Database

I used the document-based cloud database [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for this project.

My database called workouts consists of the following two collections: exercises, users.

Exercise collection holds all the information for each of the exercises and user collection holds the login information of each registered user.

### Exercise collection

| Key in DB | Data Type |
--- | ---
_id | ObjectId
category_name | String
exercise_name | String
muslces | String
exercise_difficulty | String
equipment | String
exercise_instructions | String
added_by | String
like | Array
dislike | Array
like_total | Int
dislike_total | Int

### Users collection

| Key in DB | Data Type |
--- | ---
_id | ObjectId
username | String
password | String

## Features

### Existing Features

#### Page Structure

- **Navbar:** Using Materialize the navbar is fixed at the top and collapses on medium and small devices. It is then accessible through a sidepanel that slides in from the left. If a user is logged in the navbar contains a brand logo, the website's name and the links to 'Home', 'All Exercises', 'My Exercises' and 'Logout'. If a user has not logged in the links 'Home', 'Login' and 'Register' are visible.

- **Footer:** The footer contains the education disclaimer and a GitHub link.

#### Forms

- **Register form:** enables users to create an account in order to use the app. The input fields are username and password (password needs to be repeated to confirm it).

- **Login form:** enables existing users to login and use the website.

- **Add exercise form:** enables users to add their own exercises that they want to share with other users.

- **Edit exercise form:** enables a user to edit and update their own exercises.

#### Buttons

- **Like and Dislike buttons:** enables users to like and dislike exercises. Liked exercises are then displayed in the user's My Exercises page. In the individual muscle group pages the exercises are sorted by likes, displaying the most liked exercises on the top.

- **Add Exercise button:** enables the user to add an exercise to the database.

- **Edit and Delete buttons:** each exercise a user has added when clicking on the edit button the user is able to edit and update the exercises. The delete button enables the user to fully delete the exercise from the database.

- **Delete Account button:** enables the user to delete the account including the exercises the user has added. additionally every like/dislike is removed.

- **Cancel button:** enables the user to cancel when editing an exercise

- **Back to top button:** enables the user to jump back to the top. This feature is escpecially helpful when many exercises will have been added.

#### Other

- **Materialize cards:** the exercises are displayed using Materialize cards feature.

- **Delete modal:** pop up window that asks the user if really sure before deleting the user account.

### Features Left to Implement

- Functionality of liking/disliking an exercise and staying on the same page.

- Feature to reset password, if user has forgotten password

## Technologies Used

1. HTML - this standard markup language was used for the structure and layout of this website

2. CSS - to describe the style of the HTML document

3. JavaScript - to enable interactive features in my website, such as e.g. the 'back to the top' button, delete modal and the side Navbar

4. Python - this back end programming language was used to write the route functions

5. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - a modern designer-friendly templating language for Python

6. [Materialize](https://materializecss.com/) - a modern responsive front-end framework based on Material Design. With its fluid responsive grid system Materialize was used to build the grid layout of the website. Other Materialize features used for this website are buttons, forms, navbar, footer, cards.

7. [jQuery](https://jquery.com/) - used to initialize elements of the Materialize framework

8. [Flask](https://flask.palletsprojects.com/en/1.1.x/) - a micro web framwork written in Python. F

9. [Flask-login](https://flask-login.readthedocs.io/en/latest/) - used for the tasks of loggin in, loggin out and remembering the users' sessions

10. [MongoDB Atlas](https://cloud.mongodb.com/) - a fully-managed document-oriented cloud database

11. [Github](https://github.com/) - used for development version control using Git.

12. [Heroku](https://heroku.com) - this cloud platform was used to run the deployed application

13. [Gitpod](https://www.gitpod.io/) - this online IDE was used for the development of this application

14. [Balsamiq](https://balsamiq.cloud/) - this web-based mockup tool was used to visualize the layout and design of the website

## Testing

### Code Validation

#### HTML

The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate HTML code.

#### CSS

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate CSS code. It showed two errors and several errors for the Materialize library.

A couple of errors poped up, as e.g. a duplicate " in the class in the navbar. The warning "The type attribute is unnecessary for JavaScript resources." was displayed referencing the script tag. The type="text/javascript" was therefore removed.

No errors nor warnings remained.

#### JavaScript

[JSHint](https://jshint.com/) was used to validate JavaScript. 

#### Python



### Features testing

### Responsiveness testing

### User stories testing

#### User story 1
- Each user can create their own account by clicking on 'Register' and filling out the register form. In order to register the user needs to input a new username that has not been used yet and enter a password, which needs to be repeated to confirm. Once registered the user is redirected to the login page, where he / she can log in.

#### User story 2
- On the 'My Exercises' page the user is able to delete the user account by clicking the 'Delete Account' button and confirming in the pop up window. With doing this all added exercises and votes are removed as well.

#### User story 3
- By clicking on the 'Login' button and filling out the Login form with an existing username and password any user can log in to see all exercises that are available in the database. Without being logged in it is not possible to access the exercises. Having a 'Logout' button in the navbar on the top makes it easy for the user to log out once he / she is done.

#### User story 4
- With the 'All Exercises' button in the navbar users are able to access the exercises. The 'All Exercises' page loads a bit slower even though the image sizes were reduced.

#### User story 5
- Exercises are categorized in four different categories. By clicking on one of the four muscle groups the user is able to then see exercises specific to that muscle group. 

#### User story 6
- On the bottom of each of the four muscle group exercise pages as well as on the 'My Exercises' page there is an 'Add a New Exercise' button that enable the user to add an own exercise. After filling out the exercise form the user is able to add the exercise to the database and share it with others.

#### User story 7
- Each exercise that has been added by a user can be edited by that user by clicking the 'Edit' button underneath the exercise. The user will be redirected to the edit form where information can be changed. When clicking the 'Save Changes' button on the bottom the exercise will be updated in the database. 

#### User story 8
- In the same way that a user is able to edit his / her exercises, he / she is also able to delete the exercises that he / she created by pressing the 'Delete' button.

#### User story 9
- Users are only able to edit / delete their own exercises. They are not able to edit or delete exercises that were added by others. They are however able to see who has added the exercise to the database.

#### User story 10
- Users can like or dislike each of the exercises by clicking the thumbs up / thumbs down button, which are located under the exercise names. When having liked an exercise the thumbs up button will be displayed in green. After disliking an exercise the thumbs down button will be shown in red. After liking an exercise the user is redirected to the 'My Exercises' page, where he / she is able to see all liked exercises in one place. After having clicked the dislike button the users are then redirected to the 'All Exercises' page, where they are able to look for other exercises to like.

#### User story 11
- After having liked / disliked an exercise and the user changes his / her mind by clicking on the highlighted like / dislike button it is possible to remove the like or dislike vote for the specific exercise.

#### User story 12
- When clicking on the 'My Exercises' button in the navbar the user is able to see his / her user page. Here all the exercises the user has liked are displayed on the top. Below that all exercises the user has added are being shown.

#### User story 13
- On each of the individual muscle group pages the exercises are sorted by likes. That means the exercises that have collected the most likes are displayed ot the top showing the user which exercises are favorized by the community.

## Deployment

### GitHub

I was developing the app using Gitpod. In order to keep records of the different versions during the development phase git version control was used.

Starting this project the Code Institute [Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used. Having had the Gitpod extension installed for Chrome the template was opened in Gitpod.

The following commands were taken to save the various changes in the local repository:

- `$ git add 'filename'` to add the updated files to the staging area
- `$ git commit -m "..."` to commit the changes
- `$ git push -u origin master` to push all committed changes to the remote repository on GitHub.

### Heroku

This app is hosted using Heroku.

Following steps were taken to deploy my project:

1. Create app

    - On the Heroku website I created a new app.
    - Under the 'Settings' tab I clicked the 'Reveal Config Vars' where I set the IP to 0.0.0.0 and the PORT to 5000.
    - Finally I added the MongoDB database configuration, in particular 'MONGO_DBNAME', 'MONGO_URI' and 'SECRET_KEY'

2. Login to the Heroku account in Gitpod

    - To log in to Heroku I used this command `$ heroku login -i` and entered my account details.

3. Git repository

    - I then used following command for the initial commit: `$ git commit -m "Initial Commit"`
    - and then typed `$ heroku git:remote -a 'app_name'` to set up the remote repository
    - In case the repository has not been created the following commands should be used:

        ```
        $ cd 'directory-name'/
        $ git init
        $ heroku git:remote -a 'app-name''
        ```

4. Requirements.txt

    - For Heroku to run the app we need to create a file with all the dependencies: 'requirements.txt'
    - This file is created by using the following code: `$ pip3 freeze--local > requirements.txt`

5. Procfile

    - Heroku additionally needs Procfile, which tells Heroku how to run the project.
    - In order to create Profile use this command in the terminal: `$ echo web: python app.py > Procfile`
    - Then run `$ heroku ps:scale web=1` to start web processes

6. Deployment

    - Similary to GitHub, changes were added and committed
    - With `$ git push heroku master` the committed code was pushed to Heroku.

## Credits

### Content

Information about exercises was taken from the workout app [Bodyweight Training](https://apps.apple.com/us/app/bodyweight-training-your-gym/id416981420).

### Media

The pictures where taken from the online image libraries [Pexels](https://www.pexels.com) and [Unsplash](https://unsplash.com).

### Acknowledgements

The login functionality was added with the help of the [flask-login doumentation](https://flask-login.readthedocs.io/en/latest/), this [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins) and this [Stack Overflow Thread](https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb).

The code for the back to top button was taken from [here](https://codepen.io/tomscholz/pen/qrgOKz?editors=1010).

To create the environment variables I followed [these instructions](https://code-institute-room.slack.com/archives/CP07TN38Q/p1576743936008200) of Anna Greaves, a Tutor from Code Institute.

For setting up flash messaging I used [this information](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).

Information about Flask WTF was acquired from [here](https://hackersandslackers.com/flask-wtforms-forms/).

The information from [this stackoverflow example](https://stackoverflow.com/questions/52226293/jinja2-check-if-value-exists-in-list-of-dictionaries/52229128) was used to check if the username of the current user is in the exercise like variable.

The delete modal was built with this template [How to create a Modal Box](https://www.w3schools.com/howto/howto_css_modals.asp).