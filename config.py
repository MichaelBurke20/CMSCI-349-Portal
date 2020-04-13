# The configuration settings are defined as class variables inside the Config class
# As the application needs more configuration items, they can be added to this class
# Flask-WTF extension uses SECRET_KEY to protect web forms against Cross-Site Request Forgery
# The secret key is supposed to be secret, as the strength of the tokens and signatures generated with it depends on no
# person outside trusted maintainers of the application knowing it
import os


# First, look for value of an environment variable (SECRET_KEY)
# Second, if the environment does not define the variable, then the hardcoded string is used instead
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
