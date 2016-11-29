# creating instance of the Flask
from flask import Flask
#, request, send_from_directory
# , static_url_path = ''
app = Flask(__name__) 
# setting up app

# use of config file created
app.config.from_object('config')

#importing views
from app import views

