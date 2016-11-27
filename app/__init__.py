# creating instance of the Flask
from flask import Flask
#, request, send_from_directory
# , static_url_path = ''
app = Flask(__name__) 
# setting up app

#importing views
from app import views

