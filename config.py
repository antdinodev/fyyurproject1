import os
from utilities import login

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

port = "localhost:5432"
database = "fyuur"

connection_uri = f"postgresql://{login.USER}:{login.SECRET_KEY}@{port}/{database}"


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = connection_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
