# Import the Flask class from the flask module
# Flask is the core class that creates a web application instance
from flask import Flask
import os # to work with operating system functionality

# an instance of the Flask class
# __name__ is a Python predefined variable that is set to the module name
# Flask uses this to determine the root path of the application
app = Flask(__name__)

# Generate a random 32-byte string to use as a secret key
SECRET_KEY = os.urandom(32)
# Configure the Flask application with the secret key
# used for keeping client-side sessions secure
app.config['SECRET_KEY'] = SECRET_KEY

# avoids circular import issues since these modules need to import the app variable
from application import routes
from application import errors
