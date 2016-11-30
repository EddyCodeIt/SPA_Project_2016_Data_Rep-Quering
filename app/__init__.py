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

# use of config file created
app.config.from_object('config')

# Source: http://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
# To suppress overhead warning. By default True, but need to specify: 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_MIGRATE_REPO'] = True

# creating object to store database
db = SQLAlchemy(app)
import os 
## LOGIN ##
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from config import basedir

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#importing views
from app import views, models

