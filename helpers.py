import re
import os
from flask import redirect, render_template, request, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def validate_password(password):
  if not password:
      raise AssertionError('Password not provided')

  if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
      raise AssertionError('Password must contain 1 capital letter and 1 number')

  if len(password) < 8 or len(password) > 50:
      raise AssertionError('Password must be between 8 and 50 characters')

 
def validate_username(username, db, countries):
  if not username:
      raise AssertionError('No username provided')

  if db.execute("SELECT username FROM users WHERE username = :username LIMIT 1", {"username": username}).rowcount != 0:
    raise AssertionError(f'The username you provided is already in use')

  if len(username) < 5 or len(username) > 20:
    raise AssertionError('Username must be between 5 and 20 characters')
    
  return username


def validate_email(email):
  if not email:
    raise AssertionError('No email provided')

  if not re.match("[^@]+@[^@]+\.[^@]+", email):
    raise AssertionError('Provided email is not an email address')

  return email

  