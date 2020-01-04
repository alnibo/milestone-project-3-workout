import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = 'workout'

"""
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "workout"
COLLECTION_NAME = "exercises"
"""

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    """
    Allows user to view the home page, where they can select among the workout groups.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
