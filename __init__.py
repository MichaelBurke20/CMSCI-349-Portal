# Create the application object as an instance of class Flask imported from the flask package
from flask import Flask
from config import Config

# The __name__ variable passed to the Flask class is a Python predefined variable. __name__ is set to the name of the
# module in which it is used. Flask uses the location of the module passed here as a starting point when it needs to
# load associated resources like template files

app = Flask(__name__)
# Need to tell Flask to read and apply the config file
app.config.from_object(Config)

# Bottom import works around circular imports, a common problem with Flask apps
from app import routes