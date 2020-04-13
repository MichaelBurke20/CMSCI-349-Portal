from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Optional, Email


# User log in form that asks the user to enter a username, password
# Form will also include a "remember me" checkbox and a submit button
# DataRequired validator checks that the field is not submitted empty
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class StaffLoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    department = SelectField("Department: ", choices=[("CS", "Computer Science"), ("MATH", "Mathematics"),
                                                      ("ENG", "English"), ("HIS", "History")], validators=
                             [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class HelpForm(FlaskForm):
    question = TextAreaField("Please enter your question: ", validators=[Optional()])
    email = StringField("Enter your email for a reply back: ", validators=[Email(), DataRequired()])
    submit = SubmitField("Send your question")


class AddForm(FlaskForm):
    term = SelectField("Term: ",
                       choices=[("Spr20", "Spring 2020"), ("Sum20", "Summer 2020"), ("Fall20", "Fall 2020")],
                       validators=[DataRequired()])
    title = StringField("Name of class: ", validators=[DataRequired()])
    department = SelectField("Department: ", choices=[("CS", "Computer Science"), ("MATH", "Mathematics"),
                                                      ("ENG", "English"), ("HIS", "History")], validators=
                             [DataRequired()])
    division = SelectField("Division: ", choices=[("UG", "Undergraduate"), ("G", "Graduate"), ("SEM", "Seminary")],
                           validators=[DataRequired()])
    submit = SubmitField("Search")


class DropForm(FlaskForm):
    choice = StringField("Type name of class you want dropped: ", validators=[DataRequired()])
    check = RadioField("Are you sure you want to drop? ", choices=[("YES", "Yes"), ("NO", "No")],
                       validators=[DataRequired()])
    submit = SubmitField("Drop class")