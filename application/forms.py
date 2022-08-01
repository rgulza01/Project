
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.widgets import TextArea 
from wtforms.validators import DataRequired, Length, Email, EqualTo 


class UserForm(FlaskForm):
    name_box = StringField("Enter your full name (this will also be the name you use to post very gluten free stories): ", validators=[DataRequired(), Length(min=3, max=80)])
    email_box= StringField("Email address here: ", validators=[DataRequired(), Email()])
    password_box= PasswordField("Choose a password: ", validators=[DataRequired(), EqualTo("password_box_again", message="Make sure you passwords match!")])
    password_box_again =PasswordField("Write the same password again: ", validators=[DataRequired()])
    submit_button = SubmitField("Submit")

class UserFormUpdate(FlaskForm):
    name_box = StringField("Enter the new name: ", validators=[DataRequired(), Length(min=3, max=80)])
    email_box= StringField("Enter the new email address: ", validators=[DataRequired(), Email()])
    submit_button = SubmitField("Submit")

class PostForm(FlaskForm):
    title_box = StringField("Enter the title of the post: ", validators=[DataRequired(), Length(min=3, max=300)])
    content_box = StringField("Enter your post here: ", validators=[DataRequired()], widget=TextArea())
    author_box = StringField("Enter your name as inserted for signing up: ", validators=[DataRequired(), Length(min=3, max=190)])
    slug_box = StringField("Slug: ", validators=[DataRequired()])
    submit_button = SubmitField("Submit")

#feature-3
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email_box= StringField("The same email address used during registration: ", validators=[DataRequired(), Email()])
    password_box = StringField("The password chosen during registration: ", validators=[DataRequired()])
    submit_button = SubmitField("Submit")