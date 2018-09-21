import os
import requests

from flask import Flask, session, render_template, jsonify, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

# Custom functions
from helpers import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Establish API KEY from goodreads.com
api_key = "K3Vcr1bUtGxwuMZLAZFFA"


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/login")
def login():
   return render_template("login.html")

@app.route("/logout")
def logout():
   return render_template("logout.html")

"""@app.route("/register", methods = ['POST', 'GET'])
def register_user():

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure username was submitted
        if not request.form.get("name"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)


        # Convert original password to a hash
        hash_pass = generate_password_hash(request.form.get("password"))

        # Insert register
        result = db.execute("INSERT INTO users (name, address_id, username, password) VALUES (:name, :address_id, username, password)",
        {"name": name, "address_id": 1, "username": username, "password": hash_pass})

        if not result:
            return apology("You are already registered", 400)

        # Remember which user has logged in
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    else:
         #Get countries lists json response from restcountries API
        countries = requests.get("https://restcountries.eu/rest/v2/all", params={"fields": "name"})

        return render_template("register.html", countries=countries.json())"""

        

@app.route("/register", methods = ['POST', 'GET'])
def register_user():

    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        countries = requests.get("https://restcountries.eu/rest/v2/all", params={"fields": "name"})

        try:
            validate_username(username, db, countries)
        except AssertionError as e:
            return render_template("register.html", error=str(e)) 

        # Insert register
        #result = db.execute("INSERT INTO users (name, address_id, username, password) VALUES (:name, :address_id, username, password)",
        #{"name": name, "address_id": 1, "username": username, "password": hash_pass})

        if not result:
            return apology("You are already registered", 400)

        # Remember which user has logged in
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    else:
         #Get countries lists json response from restcountries API
        countries = requests.get("https://restcountries.eu/rest/v2/all", params={"fields": "name"})

        return render_template("register.html", countries=countries.json())
    

    