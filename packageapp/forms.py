from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired

class SigninForm(FlaskForm):
    user_name = StringField('Enter your Username', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
