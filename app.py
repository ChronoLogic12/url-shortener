import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, 
    jsonify, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def shorten():
    url = mongo.db.urls.find_one(
        {"reference": "123456"})
    return render_template("shortener.html")


