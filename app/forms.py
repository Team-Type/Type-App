from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import pyrebase 

config = {
  "apiKey": "AIzaSyAQiMgNWCj9oC68LNQk4UxbkykkxS3j1pk",
  "authDomain": "type-app-b8a6b.firebaseapp.com",
  "databaseURL": "https://type-app-b8a6b.firebaseio.com",
  "projectId": "type-app-b8a6b",
  "storageBucket": "type-app-b8a6b.appspot.com",
  "messagingSenderId": "385822343582",
  "appId": "1:385822343582:web:b3cac016c93e8dcaecd68f",
  "measurementId": "G-HSC2JJ3MLC"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')