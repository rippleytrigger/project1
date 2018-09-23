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

# Aditional Debugger
from flask_debugtoolbar import DebugToolbarExtension
app.debug = True
app.config["SECRET_KEY"] = "DontTellAnyone"

toolbar = DebugToolbarExtension(app)

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
api_key = os.getenv("API_KEY_GOODREADS")


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    """Login user"""
    if request.method == "POST":

        # Forget any user_id
        session.clear()

        if request.method == "POST":

            # Ensure username was submitted
            if not request.form.get("username"):
                return jsonify({"message": "must provide username", "status": 403}) 

            # Ensure password was submitted
            elif not request.form.get("pass"):
                return jsonify({"message": "must provide password", "status": 403}) 

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = :username", {"username" : request.form.get("username") }).fetchone()
            rows = dict(rows)

            # Ensure username exists
            if rows is None:
                return jsonify({"message": "invalid username", "status": 403}) 

            # Ensure password is correct
            if not check_password_hash(rows['password'], request.form.get("pass")):
                return jsonify({"message": "invalid password", "status": 403}) 

            # Remember which user has logged in
            session["user_id"] = rows['user_id']

            # Redirect user to home page
            return redirect("/search")
    else:
        return render_template("login.html")

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
    
        
@app.route("/register", methods = ['POST', 'GET'])
def register_user():
    """Register user"""
    if request.method == "POST":
        
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("pass")
        #email = request.form.get("email")

        try:
            validate_username(username, db)
            validate_password(password)
            #validate_email(email)
        except ValueError as e:
            return jsonify({"message": str(e), "status": 400}) 

        # Convert original password to a hash
        hash_pass = generate_password_hash(password)

        # Insert user
        db.execute("INSERT INTO users (name,username, password, role_id) VALUES (:name, :username, :password, :role_id)",
        {"name": name, "username": username, "password": hash_pass, "role_id": 1})

        db.commit()

        # Get user id from db
        user_id = db.execute("SELECT user_id FROM users WHERE username = :username",
        {"username": username }).fetchone()

        print(user_id)

        # Remember which user has logged in
        session["user_id"] = user_id

        # Redirect user to home page
        return redirect("/")

    else:
         #Get countries lists json response from restcountries API
        countries = requests.get("https://restcountries.eu/rest/v2/all", params={"fields": "name"})

        return render_template("register.html", countries=countries.json())
    

@app.route("/search", methods = ['POST', 'GET'])
@login_required
def search():
    """Search book"""
    if request.method == "POST":

        search = request.form.get("search-input")

        rows = db.execute(f"SELECT * FROM books WHERE LOWER(author) LIKE '%{search.lower()}%'").fetchall()
        rows = dict(rows)

        return jsonify(rows)

    else:
        return render_template("search.html")