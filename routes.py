# The routes are different URLs that the application implements
# In Flask, handlers for the application routes are written as Python functions, called view functions
# View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests
# a given URL
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, StaffLoginForm, HelpForm, AddForm, DropForm


# A decorator modifies the function that follows it. A common pattern with decorators is to use them to register
# functions as callbacks for certain events. The @app.route decorator creates an association between the URL given as
# an argument and the function. In this case, when a web browser requests either of these two URLs, Flask is going to
# invoke this function and pass the return value of it back to the browser as a response.
@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Mount student"}
    # The operation that converts a template into a complete HTML page is called rendering
    # The render_template function takes a template file name and a variable list of arguments, returns the same
    # template, with all the placeholders {{ }} in it replaced with actual values
    return render_template("index.html", title="Home", user=user)


@app.route("/blog")
def blog():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Did anyone get in Discrete Math?'
        },
        {
            'author': {'username': 'Susan'},
            'body': "Can't wait for Algorithms with Heinold!"
        },
        {
            'author': {'username': 'Joe'},
            'body': "Professor Portier rocks!!"
        }
    ]
    return render_template("blog.html", title="Mount Portal Blog", posts=posts)


# Imported the LoginForm class from forms.py
# Instantiated an object from it, sent it down to the template
# Methods argument tells Flask that this view function accepts GET and POST requests, overriding the default (only GET)
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Gathers all the data, run all the validators attached to the fields,
        # will return True if everything is alright
        # flash function is a useful way to show a message to the user
        flash("Login requested for user {}, remember_me = {}".format(
            form.username.data, form.remember_me.data))
        # redirect function instructs the client web browser to automatically navigate to a different page, given as an
        # argument
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/staffLogin", methods=["GET", "POST"])
def staffLogin():
    form = StaffLoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, department = {}, remember_me = {}".format(
            form.username.data, form.department.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("staffLogin.html", title="Sign In - Staff", form=form)


@app.route("/helpPage", methods=["GET", "POST"])
def helpPage():
    form = HelpForm()
    if form.validate_on_submit():
        flash("Data entered was {}, reply going to email address: {}".format(
            form.question.data, form.email.data))
        return redirect(url_for("index"))
    return render_template("help.html", title="Portal Help", form=form)


@app.route("/view", methods=["GET", "POST"])
def view():
    classes = [
        {
            'className': "Algorithms",
            'classCode': "CMSCI 453 A",
            'professor': "Heinold",
            'days': "TH",
            'time': "2:00-3:15",
            'location': "COAD 107"
        },
        {
            'className': "Discrete Math",
            'classCode': "MATH 228 A",
            'professor': "Portier, Fred",
            'days': "MWF",
            'time': "9:00-9:50",
            'location': "COAD 125"
        },
        {
            'className': "Modernity in Literature",
            'classCode': "ENMO 300 B",
            'professor': "Wehner",
            'days': "MWF",
            'time': "12:00-12:50",
            'location': "AC 205"
        },
        {
            'className': "Introduction to Data Science",
            'classCode': "DATA 200 A",
            'professor': "Portier, Rebecca",
            'days': "TH",
            'time': "8:00-9:15",
            'location': "COAD 110"
        }
    ]
    return render_template("schedule.html", title="My Schedule", classes=classes)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        flash("Data entered was -> term: {}, title: {}, department: {}, divison: {}".format(
            form.term.data, form.title.data, form.department.data, form.division.data))
        return redirect(url_for("index"))
    return render_template("add.html", title="Add Classes", form=form)


@app.route("/drop", methods=["GET", "POST"])
def drop():
    form = DropForm()
    if form.validate_on_submit():
        flash("Data entered was -> choice: {}, check: {}".format(form.choice.data, form.check.data))
        return redirect(url_for("index"))
    return render_template("drop.html", title="Drop Classes", form=form)
