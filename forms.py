from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,\
    BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class LoginStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class addClassForm(FlaskForm):
    header = "Welcome To The Mount Portal"
    instruction = "Select a major from the dropdown menu: "
    Major = SelectField('Major: ', choices= [("CompSci", "Computer Science"), ("Data", "Data Science"), ("Eglsh", "English"), ("Math", "Mathematics"), ("Span", "Spanish")], validators=[DataRequired()])
    Year = RadioField('Please select your class year', choices=[("Freshman","Freshman"),("Sophomore","Sophomore"),("Junior","Junior"),("Senior","Senior")], validators=[DataRequired()])
    Link = "Here are available links for students: "
    submit = SubmitField('Add Class')