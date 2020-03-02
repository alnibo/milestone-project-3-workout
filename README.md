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

### Features Left to Implement

## Technologies Used

1. HTML
2. CSS
3. JavaScript
4. Python
5. Materialize
6. Flask
7. Flask-login
8. MongoDB Atlas
9. Github
10. Heroku

## Testing

## Deployment

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