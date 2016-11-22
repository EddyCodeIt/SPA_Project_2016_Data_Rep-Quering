from random import randint

from app import app 
#send_from_directory

@app.route("/") 
# URL for website navigation
def root():
    return app.send_static_file("index.html")

