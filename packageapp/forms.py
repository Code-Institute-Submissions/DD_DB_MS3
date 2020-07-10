from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired


class SigninForm(FlaskForm):
    username = StringField('Insert Username', validators=[DataRequired()])
    password = PasswordField('Insert Password', validators=[DataRequired()])


class SignupForm(FlaskForm):
    username = StringField('Insert Username', validators=[DataRequired()])
    password = PasswordField('Insert Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])
