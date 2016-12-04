# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
# importing db object
from app import db
from flask_login import UserMixin

# creating a class, simillar to a java bean class, acts as a structure of database table.
# here we pass db object (ref __init__) with sqlalchemy tools like Model, Column
class User(db.Model, UserMixin):
    __tablename__ = "users"
    # "table" structure, normal variables for python
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(15), index=True, unique=True)
    password = db.Column('password', db.String(15))
    
#setting ()
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def set_password(self , password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password , password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)