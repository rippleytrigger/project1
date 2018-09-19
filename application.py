import os
import requests

from flask import Flask, session, render_template, jsonify, request
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

@app.route("/register", methods = ['POST', 'GET'])
def register_user():

    if request.method == 'GET':
        
        #Get countries lists json response from restcountries API
        countries = requests.get("https://restcountries.eu/rest/v2/all", params={"fields": "name"})

        return render_template("register.html", countries=countries.json())
        
    else:

        addresses = []

        for address in request.form.to_dict():
            addresses.append(request.form.to_dict()[address])
            print(addresses)

        """ Addresses POST Data """
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        country = request.form.get('countries')
        state = request.form.get('state')
        postal_code = request.form.get('postal_code')

        """ User POST Data """
        name = request.form.get('address1')
        username = request.form.get('username')
        password = request.form.get('username')

        try:
            validate_username(username)
            validate_password(password)
            validate_email(email)
        except AssertionError:
            print ("The name that you put is the form is not valid")
            return render_template("register.html")
        


        #Insert Address on DB
        #db.execute("INSERT INTO addresses (address1, address2, country, state, postal_code) VALUES (:address1, :address2, :country, :state, :postal_code)",
        #{"address1": address1, "address2": address2, "country": country, "state": state, "postal_code": postal_code})

        #Insert User on DB
        #db.execute("INSERT INTO users (name, address_id, username, password) VALUES (:name, :address_id, username, password)",
        #{"name": name, "address_id": address_id, "username": username, "password": password})

        db.commit()
        
        return render_template("register.html")   

    

    