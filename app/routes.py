from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
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

@app.route('/')
@app.route('/home')
def index():
    users = {'username': 'Luke'}
    posts = [
        {
            'author': {'username': 'Nathan'},
            'body': 'Hockey is the best.'
        },
        {
            'author': {'username': 'Dom'},
            'body': 'No, running is.'
        }
    ]
    return render_template('home.html', title='Home', user=users, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #user = auth.sign_in_with_email_and_password(username, password)
    #auth.get_account_info(user["idToken"])
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

