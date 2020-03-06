from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


# Login Form

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(
                               "Please enter a valid username")])
    password = PasswordField('Password',
                             validators=[DataRequired(
                                 "Please enter your password")])
    submit = SubmitField('Login')


# Registration Form

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=5, max=50)])
    password2 = PasswordField('Confirm Password',
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
