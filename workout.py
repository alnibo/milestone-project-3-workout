import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = 'workout'

"""
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "workout"
COLLECTION_NAME = "exercises"
"""

mongo = PyMongo(app)

# Index/home

@app.route('/')
@app.route('/index')
def index():
    """
    Home page - landing page
    """
    return render_template('index.html')


# Register new account

@app.route('/register')
def register():
    """
    Enables user to register a new account.
    """
    return render_template('register.html')


# Login with existing account

@app.route('/login')
def login():
    """
    Allows user to login with existing account.
    """
    return render_template('login.html')


# Muscle groups

@app.route('/muscle_groups')
def muscle_groups():
    """
    Allows user to view the muscle groups.
    """
    return render_template('groups.html')


# Set up of IP address and PORT number

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
