import re
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

"""class form_checker:
  def __init__(self, name, age):
    self.name = name
    self.age = age"""

def set_password(password):
  return generate_password_hash(password)

def check_password(password):
  return check_password_hash(password_hash, password)



def validate_password(password):
  if not password:
      raise AssertionError('Password not provided')

  if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
      raise AssertionError('Password must contain 1 capital letter and 1 number')

  if len(password) < 8 or len(password) > 50:
      raise AssertionError('Password must be between 8 and 50 characters')


def validate_username(username):
  if not username:
      raise AssertionError('No username provided')

  username_db = db.execute("SELECT username FROM users WHERE username = :username LIMIT 1",
  {"username": username})

  print(username_db)

  if username_db:
    raise AssertionError(f'{username_db} is already in use')

  if len(username) < 5 or len(username) > 20:
    raise AssertionError('Username must be between 5 and 20 characters')

  return username


def validate_email(email):
  if not email:
    raise AssertionError('No email provided')

  if not re.match("[^@]+@[^@]+\.[^@]+", email):
    raise AssertionError('Provided email is not an email address')

  return email

  