# creating instance of the Flask
from flask import Flask
#  send_from_directory -> instead of jinja to get static files

# For SqlAlchemy to work need:
    # 1) Install SqlAlchemy
    # 2) Install SqlAlchemy-migrate
    # 3) Install Flask-SqlAlchemy
    # Everything can be installed using pip command   
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
# setting up app

# use of config file
app.config.from_object('config')

# Source: http://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
# To suppress overhead warning. By default True, but need to specify: 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_MIGRATE_REPO'] = True
# Storing instance of the database in global variable db. Now we can use SQLAlchemy commands to build database and interact with it.
db = SQLAlchemy(app)
# importing object that stores path to directory with database migrate files. Note: need to check if its ever used... 
from config import basedir
# for OS paths manipulations
import os 
## LOGIN - manager and password-hashing security ##
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

# Making instance of Manager and initializing it in app.  
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'   
# ^                            
# |__ binding 'login' view to manager

#importing views and models
from app import views, models

