import os
import string
import random
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

def generateReference(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))


@app.route("/")
def home():
   return redirect(url_for("shorten"))

@app.route("/shortener", methods=["GET", "POST"])
def shorten():
    if request.method == "POST":
        urlLong = request.form.get("url-long")
        
        if mongo.db.urls.find_one({"url": urlLong}):
            flash("message")
            return redirect(url_for("shorten"))
    url = mongo.db.urls.find_one(
        {"reference": "123456"})
    return render_template("shortener.html")

# @app.route("/<string:reference>")
# def redirectToPage(reference):
#     try:
#         url = mongo.db.urls.find_one(
#         {"reference": reference})
#         redirect()

# print(generateReference(20))
