from flask import render_template
from app import app 
from .content_manager import Content
#send_from_directory

TOPIC_DICT = Content()

# URL for website navigation
@app.route('/')
@app.route('/home')
def index(): 
    return render_template("index.html")

@app.route('/header/')
def header():                                              
    return render_template("header.html", TOPIC_DICT = TOPIC_DICT)
    # 1st TOPIC_DICT is used in html 
    # 2nd TOPIC_DICT is corresponding to one declared on top
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")