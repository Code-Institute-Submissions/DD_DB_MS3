from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SigninForm(FlaskForm):
    username = StringField("Insert Username",
                           validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField("Insert Password",
                             validators=[DataRequired(), Length(min=4)])


class SignupForm(FlaskForm):
    username = StringField("Insert Username",
                           validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Insert E-mail', validators=[DataRequired(), Email()])
    password = PasswordField("Insert Password",
                             validators=[DataRequired(), Length(min=4)])
    password2 = PasswordField("Repeat Password",
                              validators=[DataRequired(), EqualTo("password")])
