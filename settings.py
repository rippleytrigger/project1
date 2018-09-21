import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def init():
    # Check for environment variable
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")

    # Set up database
    global db
    engine = create_engine(os.getenv("DATABASE_URL"))
    db = scoped_session(sessionmaker(bind=engine))

    # Establish API KEY from goodreads.com
    global api_key
    api_key = "K3Vcr1bUtGxwuMZLAZFFA"
    
init()