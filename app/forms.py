#from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min = 4, max = 20), validators.Required()], id = "input_fields")
    password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo('confirm', message = "Passwords must match")], id = "input_fields")
    confirm = PasswordField('Repeat Password', id = "input_fields")
