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


    
# User profile
@app.route("/user-profile/<username>")
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        flash("User %s not found." % username)
        return redirect(url_for("index"))
    return render_template("user-profile.html", user=user)

@app.route('/topics/')
@login_required
def topics():
    return render_template("topics.html", TOPIC_DICT = TOPIC_DICT)
    # 1st TOPIC_DICT is used in html 
    # 2nd TOPIC_DICT is corresponding to one declared on top
    
@app.route('/topics/installing-components/')
@login_required
def installation():
    return render_template("/topics/installing-components.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/app-architecture/')
@login_required
def architecture():
    return render_template("/topics/app-architecture.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/coding-basics/')
@login_required
def basics():
    return render_template("/topics/coding-basics.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/app-setup-conclusion/')
@login_required
def basics_conclusion():
    return render_template("/topics/app-setup-conclusion.html", TOPIC_DICT = TOPIC_DICT)#

@app.route('/topics/about-bootstrap/')
@login_required
def about_bootstrap():
    return render_template("/topics/about-bootstrap.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/bootstrap-conclusion/')
@login_required
def bootstrap_conclusion():
    return render_template("/topics/bootstrap-conclusion.html", TOPIC_DICT = TOPIC_DICT)
    
@app.route('/topics/what-is-jinja2/')
@login_required
def about_jinja():
    return render_template("/topics/what-is-jinja2.html", TOPIC_DICT = TOPIC_DICT)
    
@app.route('/topics/how-to-jinja/')
@login_required
def how_to_jinja():
    return render_template("/topics/how-to-jinja.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/jinja2-conclusion/')
@login_required
def jinja2_conclusion():
    return render_template("/topics/jinja2-conclusion.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/sqlite-alchemy/')
@login_required
def sqlite_alchemy():
    return render_template("/topics/sqlite-alchemy.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/db-models/')
@login_required
def db_models():
    return render_template("/topics/db-models.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/flask-forms/')
@login_required
def flask_form():
    return render_template("/topics/flask-forms.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/topics/database-conclusion/')
@login_required
def database_conclusion():
    return render_template("/topics/database-conclusion.html", TOPIC_DICT = TOPIC_DICT)




# Code source: https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/
@app.route('/login/',methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('topics'))
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
    return redirect(url_for('index'))
    
# need to handle(if debug mode set to true): sqlalchemy.exc.IntegrityError
#                 IntegrityError: (IntegrityError) column username is not unique u'UPDATE user SET nickname=?, about_me=? WHE
#               (if debug mode false): HTTP error code 500
# Solution: try: ... except exc.IntegrityError as e: ... . Sqlalchemy exc library handles exceptions for us. 
# Important! rollback() current db session if IntegrityError trigger excepted. 
@app.route('/register/', methods = ['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('topics'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            user = User(form.username.data,
                        form.password.data)        
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('login'))
# http://stackoverflow.com/questions/24522290/cannot-catch-sqlalchemy-integrityerror 
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
