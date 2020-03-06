# Find Your Workout

Stream Three Project - Data Centric Development Milestone - Code Institute

![Image of Find Your Workout Home Page](https://github.com/alnibo/milestone-project-3-workout/blob/master/static/img/findyourworkout.jpg)

This website will help you get inspiration and ideas for your next workout. You will find different kinds of exercises for each muscle group and will also have to possibility to add your own exercises to the database to share with others.

## Table of Contents

1. [Demo](#1.-demo)
2. [UX](#2.-ux)
3. [Database](#3.-database)
4. [Features](#4.-features)
5. [Technologies Used](#5.-technologies-used)
6. [Testing](#6.-testing)
7. [Deployment](#7.-deployment)
8. [Credits](#8.-credits)

## 1. Demo

Check out the deployed website [here](https://find-your-workout.herokuapp.com/).

## 2. UX

To create a sleek look and a homogeneous experience for the user I used the colors black, white and grey consistently throughout the project.

In order to create an easy and intuitive user experience I designed the website in a way where it is simple for the user to use.

### Target Audience

The website targets anyone who is interested in finding out more about not only what exercises to do in order to stay fit but also how to do them and what equipment is needed. More than that, this application also enables users to create own exercises and like existing exercises in order to build up their own user page with liked and added exercises.

Therefore this application enables the user to read, add, edit and rate exercises.

### User Stories

As a user I expect/would like/need:

1. to create an account in order to access the existing exercises.

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

## 3. Database

I used the document-based cloud database [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for this project.

My database called workouts consists of the following two collections: exercises, users.

The exercise collection holds all the information for each of the exercises and the user collection holds the login information of each registered user. 

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

## 4. Features

### Existing Features

#### Page Structure

- **Navbar:** Using Materialize the navbar is fixed at the top and collapses on medium and small devices. It is then accessible through a sidepanel that slides in from the left. If a user is logged in the navbar contains a brand logo, the website's name and the links to 'Home', 'All Exercises', 'My Exercises' and 'Logout'. When clicking the 'All Exercises' button a dropdown menu appears in which the user can directly choose one of the four muscle groups. If a user is not logged in only the links 'Home', 'Login' and 'Register' are visible.

- **Footer:** The footer contains the education disclaimer and a GitHub link.

#### Forms

- **Register form:** the flask register form enables users to create an account in order to use the app. The input fields are username and two password fields (the password needs to be repeated to confirm it).

- **Login form:** the flask login form enables existing users to login and use the website.

- **Add exercise form:** form that enables users to add their own exercises that they want to share with other users.

- **Edit exercise form:** form that enables a user to edit and update their own exercises.

#### Buttons

- **Like and Dislike buttons:** enable users to like and dislike exercises. Liked exercises are then displayed in the user's 'My Exercises' page. In the individual muscle group pages the exercises are sorted by likes, displaying the most liked exercises on the top.

- **Add Exercise button:** enables the user to add an exercise to the database.

- **Edit and Delete buttons:** for each exercise a user has added when clicking on the edit button the user is able to edit and update the exercises. The delete button enables the user to fully delete the exercise from the database.

- **Delete Account button:** enables the user to delete the account. Additionally all exercises the user has added and every like and dislike is removed from the database.

- **Cancel button:** enables the user to cancel when adding or editing an exercise

- **Back to top button:** enables the user to jump back to the top. This feature is escpecially helpful when many exercises will have been added.

#### Other

- **Materialize cards:** the exercises are displayed using the Materialize cards feature.

- **Delete modal:** pop up window that asks the user if really sure before deleting the user account.

### Features Left to Implement

- Search feature in order to search for e.g. just easy exercises

- Functionality of liking/disliking an exercise and staying on the same page.

- Feature to reset password, if user has forgotten password

## 5. Technologies Used

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

## 6. Testing

### Code Validation

#### HTML

The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate HTML code.

Two errors and several warnings were shown. But these were regarding Materialize and were disregarded. 

Otherwise no errors nor warnings were shown.

#### CSS

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate CSS code. It showed two errors and several errors for the Materialize library.

A couple of errors poped up, as e.g. a duplicate " in the class in the navbar. The warning "The type attribute is unnecessary for JavaScript resources." was displayed referencing the script tag. The type="text/javascript" was therefore removed.

No errors nor warnings remained.

#### JavaScript

[JSHint](https://jshint.com/) was used to validate JavaScript.

The validator revealed that there is one undefined variable `$`. This warning was ignored as I think JSHint does not have access to external libraries, such as jQuery.

No other warnings were shown.

#### Python

The [workout_tests.py](https://github.com/alnibo/milestone-project-3-workout/blob/master/workout_tests.py) file was created to test the python code. Tests were run to test if pages were rendering correctly, if the errors for the registration and login form appear and if the login functionallity works.

All other functionalites were manually tested.

### Features testing

Throughout the development of this website all features were manually tested. The following table gives an overview of how the features were tested and lists resolved and remaining bugs.

| Page | Feature | Tests | Bugs |
| :---: | :---: | --- | --- |
| Base/general | Navbar | - test if navbar shows 'Home', 'Login' and 'Register' buttons when user is not authenticated <br> - test if navbar shows 'Home', 'All Exercises', 'My exErcises' and 'Logout' buttons <br> - test if all navbar buttons redirect to the correct page <br> - test if dropdown button works, when clicking once the dropdown options should appear, when pressing on it again it should redirect to the muscle group page and when pressing anywhere else the options should hide again <br> - test if buttons corresponding to the current page are highlighted <br>  - test if navbar collapses on smaller devices and if sideNav works | - Initially dropdown menu and sideNav menue didn't work - resolved through using correct code for the corresponding Materialize version <br> - sideNav menue was not clickable, resolved by moving the SideNav code outside the navbar-fixed div. |
| | Footer | - test if GitHub link works and redirects user to the GitHub repository when clicking the button <br> - test if page opens in a new tab | No bugs |
| | Back to Top Button | - test if button appears when scrolling down <br> - test when clicking if page gets scrolled back to the top | No bugs |
| Index | Register Button | - test if button redirects to the register form <br> - test if button is visible when user not authenticated <br> - test if button is not visible when user is authenticated | No bugs |
| | Login Button | - test if button redirects to the login form <br> - test if button is visible when user not authenticated <br> - test if button is not visible when user is authenticated | No bugs |
| | All Exercise Button | - test if button redirects to the muscle groups page <br> - test if button is visible when user is authenticated <br> - test if button is not visible when user not authenticated | No bugs |
| | My Exercises Button | - test if button redirects to the my exercises page <br> - test if button is visible when user is authenticated <br> - test if button is not visible when user not authenticated | No bugs |
| Register | Register form | - test if validator (data required) works, so when field left empty it informs the user to fill out input fields <br> - test if validator (length) works, so an error gets display when username or password are either too short or too long <br> - test if errors get displayed when inputting an existing username or when the two passwords don't match <br> - test in database that submitted data gets saved correctly in the database <br> - test on database if password is indeed being hashed <br> - test if user can register when providing the correct data and gets redirected to the login page | No bugs |
| | link to login page | - test if link correctly redirects to the login form | No bugs |
| Login | Login form | - test if validator (data required) works, so when field left empty it informs the user to fill out input fields <br> - test if errors get displayed when inputting a non existing username or a wrong password <br> - test if user can login when providing the correct data and gets redirected to the muscle groups page | No bugs |
| | link to register page | - test if link correctly redirects to the register form | No bugs |
| Muscle groups | Muscle groups Buttons | - test if all group buttons (Push, Pull, Legs, and Core) redirect to the category page <br> - test if hover functionality works | No bugs |
| Category | correct group | - check if the correct image is selected for each of the muscle groups <br> - check if heading and all exercise information is for the correct muscle group | No bugs |
| | Like /Dislike Buttons | - test if color changes after clicking the button <br> - test if username gets correctly added to the like / dislike array in the database <br> - test if user is redirected to the My Exercises page after liking an exercise <br> - test if user is redirected to the muscle groups page after disliking an exercise | Initially there was an issue with checking if a username is in the like / dislike array. This was solved with this code `if current_user.username in exercise.like\|map(attribute="username")` |
| | Total Like /Dislike Count | - test in database if count is correct <br> - test if count changes by 1 when liking / disliking an exercise | No bugs |
| | Edit Button | - check if Edit button is visible if user has added the exercise <br> - check if Edit button is not visible when another user has added the exercise <br> - test if button redirects to the edit form | No bugs |
| | Delete Button | - check if Delete button is visible if user has added the exercise <br> - check if Delete button is not visible when another user has added the exercise <br> - test if button delets the exercise from the database | No bugs  |
| | Add a New Exercise Button | - test if button redirects to the Add Exercise form | No bugs |
| Add Exercise | Add Exercise form | - test when field left empty the form won't get submitted and that the user gets informed to fill out input fields <br> - test in database that submitted data gets saved correctly in the database | - Initially there was an issue with the select field (it wouldn't show the dropdown options). Resolved through using correct code for the corresponding Materialize version. <br> - when not selecting a muscle group or exercise exercise_difficulty, the form won't get submitted but no error message gets displayed |
| | Add Exercise Button | - test if button submits the form and redirects the user back to where the user started from | No bugs |
| | Cancel Button | - test if button exits the add exercise form and redirects back to the page where the user started from | No bugs |
| Edit Exercise |Edit Exercise form | - test when field left empty the form won't get submitted and that the user gets informed to fill out input fields <br> - test in database that submitted data updates the existing in the database correctly | - inital issue with select field (as in the add exercise form). Resolved through using correct code for the corresponding Materialize version. <br> - when not selecting a muscle group or exercise exercise_difficulty, the form won't get submitted but no error message gets displayed |
| | Save Changes Button | - test if button submits the form and redirects the user to the muscle group page of the current exercise | No bugs |
| | Cancel Button | - test if button exits the edit exercise form and redirects and redirects the user to the muscle group page of the current exercise | No bugs |
| My Exercises | General | - check if current username is displayed correctly at the top of the page <br> - check if all exercises the current user has liked are displayed in the liked exercise section of the page <br> - check if all added exercises of the current user are displayed in the added exercises section | No bugs |
| | Delete Account Button | - test if by clicking the modal gets opend | No bugs |
| | Delete Account Modal | - test if user account, all added exercises and likes / dislikes are removed from the database after the user confirms the deletion <br> - test if modal closes when clicking on the Cancel Button or anywhere outside the modal <br> - check if user account is still in database after the user cancelled the deletion | No bugs |
| | Added exercises (further down link | - test if the further down link scrolls down to the added exercises section | No bugs |
| | Like /Dislike Buttons | - test if color changes after clicking the button <br> - test if username gets correctly added to the like / dislike array in the database <br> - test if user is redirected to the My Exercises page after liking an exercise <br> - test if user is redirected to the muscle groups page after disliking an exercise | Initially there was an issue with checking if a username is in the like / dislike array. This was solved with this code `if current_user.username in exercise.like\|map(attribute="username")` |
| | Total Like /Dislike Count | - test in database if count is correct <br> - test if count changes by 1 when liking / disliking an exercise | No bugs |
| | Edit Button | - check if Edit button is visible if user has added the exercise <br> - check if Edit button is not visible when another user has added the exercise <br> - test if button redirects to the edit form | No bugs |
| | Delete Button | - check if Delete button is visible if user has added the exercise <br> - check if Delete button is not visible when another user has added the exercise <br> - test if button delets the exercise from the database | No bugs  |
| | Add a New Exercise Button | - test if button redirects to the Add Exercise form | No bugs |


### Responsiveness testing

Ensuring its responsiveness this website was tested across different mobile, tablet and desktop devices using Chrome developer tools. In a second step it was then tested across the most common internet browsers (Safari, Chrome, Internet Explorer, and Firefox), making sure it is compatible. For a detailed overview, please see this excel file [here](https://github.com/alnibo/milestone-project-3-workout/blob/master/Testing-resp-comp.pdf).

### User stories testing

#### User story 1
- Each user can create their own account by clicking on 'Register' and filling out the register form. In order to register the user needs to input a new username that has not been used yet and enter a password, which needs to be repeated to confirm. Once registered the user is redirected to the login page, where he / she can log in.

#### User story 2
- On the 'My Exercises' page the user is able to delete the user account by clicking the 'Delete Account' button and confirming it in the pop up window. With doing this all added exercises and votes are removed from the database.

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

## 7. Deployment

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
    - In the heroku dashboard of my application under the 'Settings' tab I clicked on 'Reveal Config Vars', where I then set the following config vars: 
    
    key | value 
    --- | ---
    IP | 0.0.0.0
    MONGO_DBNAME | `<database_name>`
    MONGO_URI | `mongodb+srv://MongUser:<password>>@myfirstcluster-mqzsr.mongodb.net/<database_name>?retryWrites=true&w=majority`
    PORT | 5000
    SECRET_KEY | `<secret_key>`

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

### Instructions on how to run this project locally

1. Make sure you have an IDE and the following must be installed:
  - [PIP](https://pip.pypa.io/en/stable/installing/#upgrading-pip) (will be already installed if you are using Python 3.4 or above)
  - [Python 3](https://www.python.org/downloads/)
  - [Git](https://www.atlassian.com/git/tutorials/install-git)
  - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

2. Go to https://github.com/alnibo/milestone-project-3-workout. There you can either download a copy of the repository by clicking on "Download ZIP" on the top right of the page or if you have Git installed you can clone the repository with the following command:

```
git clone https://github.com/alnibo/milestone-project-3-workout.git
```

3. In your local IDE you need to create two files, one called `env.py` and the other one `.gitignore`

4. Your `env.py` file should contain a SECRET_KEY, MONGO_URI, and MONGO_DBNAME to create a link to your Mongo database. The database should be called `workout` with the collections `users` and `exercises`.

5. Make sure that your `.gitignore` file contains `env.py` so that your environment variables won't get pushed to your remote repository.

6. Then run the following command and open port in preview or in a new browser tab:

```
python3 workout.py
```

## 8. Credits

### Content

Information about exercises was taken from the workout app [Bodyweight Training](https://apps.apple.com/us/app/bodyweight-training-your-gym/id416981420).

### Media

The pictures were taken from the online image libraries [Pexels](https://www.pexels.com) and [Unsplash](https://unsplash.com).

### Acknowledgements

The login functionality was added with the help of the [flask-login doumentation](https://flask-login.readthedocs.io/en/latest/), this [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins) and this [Stack Overflow Thread](https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb).

The code for the back to top button was taken from [here](https://codepen.io/tomscholz/pen/qrgOKz?editors=1010).

To create the environment variables I followed [these instructions](https://code-institute-room.slack.com/archives/CP07TN38Q/p1576743936008200) of Anna Greaves, a Tutor from Code Institute.

For setting up flash messaging I used [this information](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).

Information about Flask WTF was acquired from [here](https://hackersandslackers.com/flask-wtforms-forms/).

The information from [this stackoverflow example](https://stackoverflow.com/questions/52226293/jinja2-check-if-value-exists-in-list-of-dictionaries/52229128) was used to check if the username of the current user is in the exercise like variable.

The delete modal was built with this template [How to create a Modal Box](https://www.w3schools.com/howto/howto_css_modals.asp).

[This Flask Testing documentation](https://pythonhosted.org/Flask-Testing/) and [this project](https://github.com/JBroks/booksy-reviews) provided guidance and laid the ground work when testing my Python code.