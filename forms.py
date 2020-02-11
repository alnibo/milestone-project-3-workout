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
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=50)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Add Exercise Form

class ExerciseForm(FlaskForm):
    category_name = SelectField('Exercise Group', validators=[DataRequired()], choices=[('Push', 'Push'), ('Pull', 'Pull'), ('Legs', 'Legs'), ('Core', 'Core')])
    exercise_name = StringField('Exercise Name', validators=[DataRequired()])
    muscles = StringField('Muscles', validators=[DataRequired()])
    exercise_difficulty = StringField('Exercise Difficulty', validators=[DataRequired()])
    equipment = StringField('Equipment', validators=[DataRequired()])
    exercise_instructions = TextAreaField('Exercise Instructions', validators=[DataRequired()])
    submit = SubmitField('Add Exercise')

"""
    def validate_username(self, username):
        user = User.mongo.db.users.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
"""
