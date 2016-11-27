from flask import render_template
from app import app 
#send_from_directory

# URL for website navigation
@app.route('/')
@app.route('/home')
def index(): 
    return render_template("index.html")

@app.route('/server-settup/install')
def action():
    return render_template("/server-settup/install.html")