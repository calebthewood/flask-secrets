from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    """Register form"""

    username = StringField("Username", validators=[
                                                InputRequired(),
                                                Length(max=100)])

    password = PasswordField("Password", validators=[
                                                InputRequired(),
                                                Length(max=100)])

    email = StringField("Email", validators=[
                                        InputRequired(),
                                        Email(),
                                        Length(max=100)])

    first_name = StringField("First Name", validators=[
                                                InputRequired(),
                                                Length(max=100)])

    last_name = StringField("Last Name", validators=[
                                                InputRequired(),
                                                Length(max=100)])

class LoginForm(FlaskForm):
    """Login form"""

    username = StringField("Username", validators=[InputRequired(),
                                                  Length(max=100)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(max=100)])

class NoteForm(FlaskForm):
    """Note form"""

    title = StringField("Note Title", validators=[InputRequired(),
                                                Length(max=100)])
    content = StringField("Content", validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """CSRF From"""
