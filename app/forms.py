from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Register')

class ProfileBuildForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  age = StringField('Age', validators=[DataRequired()])
  location = StringField('Location', validators=[DataRequired()])
  occupation = StringField('Occupation', validators=[DataRequired()])
  submit = SubmitField('Submit')