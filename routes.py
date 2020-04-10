from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, LoginStudentForm, addClassForm
@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Cam"}
    posts = [
        {
            "author": {"username": "john"},
            "body": "cool day in portland"
        },
        {
            "author": {"username": "susan"},
            "body": "avengers was dope "
        }
    ]
    return render_template("index.html", title = "home", user = user, posts = posts)

@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash ('login requested for user {}, remember_me={}'.format
               (form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/loginS', methods = ["GET", "POST"])
def loginS():
    form = LoginStudentForm()
    if form.validate_on_submit():
        flash ('login requested for user {}, remember_me={}'.format
               (form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('loginS.html',
                           title='Sign In',
                           form=form)

@app.route('/addClass', methods = ["GET", "POST"])
def addClass():
    form = addClassForm()
    if form.validate_on_submit():
        flash('user searched for: {}'.format
              (form.Major.data, form.Year.data))
        return redirect(url_for('index'))
    return render_template('addClass.html',
                           title='Addclass',
                           form=form)