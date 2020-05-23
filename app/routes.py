import flask
from flask import session
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import ProfileBuildForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from getpass import getpass
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
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        user = auth.sign_in_with_email_and_password(form.username.data, form.password.data)
        user1 = auth.get_account_info(user["idToken"])
        session['user'] = user1
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Registration requested for user {}'.format(form.username.data))
        user = auth.create_user_with_email_and_password(form.username.data, form.password.data)
        user1 = auth.sign_in_with_email_and_password(form.username.data, form.password.data)
        user2 = auth.get_account_info(user["idToken"])
        session['user'] = user2
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileBuildForm()
    if form.validate_on_submit():
        user = session.get('user')
        print(user)
        return redirect(url_for('index'))
    return render_template('profile.html', title='Profile', form=form)





