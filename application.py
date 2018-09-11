import os
import requests

# For showing messages on terminal
import sys

from flask import Flask, session, render_template, jsonify, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


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

# Establish API KEY from goodreads
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

@app.route("/register", methods = ['POST', 'GET'])
def register_user():

    if request.method != 'POST':
        
        #
        countries = requests.get("https://restcountries.eu/rest/v2/all", params={"fields": "name"})

        print(countries, file=sys.stderr)

        return render_template("register.html", countries=countries.json())
        

    return render_template("register.html")

    