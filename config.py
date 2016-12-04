# os - Miscellaneous operating system interfaces
# This module provides a portable way of using operating system dependent functionality. 
# For manipulating paths in Operating System:
import os

##### Flask-WTF extension Configurations #####
# protects application from fake cross-site request and maliciouse injections. Required for Flask-WTF extention:
CSRF_ENABLED = True
# SECRET_KEY is needed when CSRF is activated. It is used for cryptogrophy token which is used for form validation. Make sure key is hard to guess:
SECRET_KEY = 'sseug-reven-lliw-uoy'

###### DB Configurations #######
# creating variable to store 
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI - needed for Flask-SQLAlchemy extension. This is a path to a Database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO - folder to store SQLAlchemy-migrate files. 
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# SQLAlchemy-migrate package is provides tools like command line and API for DB creation. This allows us to update database easy. 