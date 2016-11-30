from flask import render_template, flash, request, url_for, redirect, session, abort, g
from app import app, db, login_manager

## LOGIN imports ##

from flask_login import login_user, logout_user, current_user, login_required
from .models import User

## CONTENT MANAGER imports ##
from .content_manager import Content
#send_from_directory

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request 
def before_request():
    g.user = current_user
    
    
TOPIC_DICT = Content()

# URL for website navigation
@app.route('/')
@app.route('/home')
def index(): 
    return render_template("index.html")

@app.route('/header/')
@login_required
def header():       
    flash("Flash test")
    return render_template("header.html", TOPIC_DICT = TOPIC_DICT)
    # 1st TOPIC_DICT is used in html 
    # 2nd TOPIC_DICT is corresponding to one declared on top
    
# Code source: https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Invalid username or password', 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(url_for('header'))
    
@app.route('/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index')) 


# 404 error handle that renders 404.html template 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
