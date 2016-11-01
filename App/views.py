from app import app


# Next line is a decorator. Adds extra functionality to a function
@app.route("/") 


# URL for website navigation
def root():
    return app.send_static_file("index.html")
