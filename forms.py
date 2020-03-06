from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length


# Login Form

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
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


# Add Exercise Form
"""
class ExerciseForm(FlaskForm):
    exercise_name = StringField('Exercise Name', validators=[DataRequired()])
    muscles = StringField('Muscles', validators=[DataRequired()])
    exercise_difficulty = SelectField('Exercise Difficulty',
                                      validators=[DataRequired()],
                                      choices=[('easy', 'easy'),
                                               ('medium', 'medium'),
                                               ('difficult', 'difficult')])
    equipment = StringField('Equipment', validators=[DataRequired()])
    exercise_instructions = TextAreaField('Exercise Instructions',
                                          validators=[DataRequired()])
    submit = SubmitField('Add Exercise')



category_name = SelectField('Exercise Group', validators=[DataRequired()],
                                choices=[('Push', 'Push'),
                                         ('Pull', 'Pull'),
                                         ('Legs', 'Legs'),
                                         ('Core', 'Core')])
category_name = StringField('Exercise Group', validators=[DataRequired()])

exercise_difficulty = StringField('Exercise Difficulty',
                                      validators=[DataRequired()])
"""
