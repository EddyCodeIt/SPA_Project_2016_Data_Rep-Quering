from flask import render_template, flash, request, url_for, redirect, session, abort, g
from app import app, db, login_manager

## LOGIN imports ##

from flask_login import login_user, logout_user, current_user, login_required
from .models import User
from .forms import RegistrationForm

# Exceptions #
from sqlalchemy import exc
## CONTENT MANAGER imports ##
from .content_manager import Content
#send_from_directory

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# The g global is setup by Flask as a place to store and share data during the life of a request. Logged in user stored there.
# Any functions that are decorated with before_request will run before the view function each time a request is received.
@app.before_request 
def before_request():
    g.user = current_user
    
    
TOPIC_DICT = Content()

# URL for website navigation
@app.route('/')
@app.route('/home/')
def index(): 
    return render_template("index.html")

@app.route('/header/')
@login_required
def header():       
    return render_template("header.html", TOPIC_DICT = TOPIC_DICT)
    # 1st TOPIC_DICT is used in html 
    # 2nd TOPIC_DICT is corresponding to one declared on top
    
# Code source: https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/
@app.route('/login/',methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('header'))
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
    
# need to handle(if debug mode set to true): sqlalchemy.exc.IntegrityError
#                 IntegrityError: (IntegrityError) column nickname is not unique u'UPDATE user SET nickname=?, about_me=? WHE
#               (if debug mode false): HTTP error code 500
# Solution: try: ... except exc.IntegrityError as e: ... . Sqlalchemy exc library handles exceptions for us. 
# Important! rollback() current db session if IntegrityError triggers excepted. 
@app.route('/register/', methods = ['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('header'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            user = User(form.username.data,
                        form.password.data)        
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('login'))
        except exc.IntegrityError as e:
            flash("That user name is already taken... Try something else!")
            db.session().rollback()
            return render_template('register.html', form=form)
    return render_template('register.html', form=form)
    

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index')) 


# 404 error handle that renders 404.html template 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
