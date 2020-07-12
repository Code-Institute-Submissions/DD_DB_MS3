from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms import DateField, IntegerField
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


class ProductForm(FlaskForm):
    brand = StringField("Brand")
    capacity = IntegerField("Capacity (ml/gr)", validators=[DataRequired()])
    datepurchase = DateField("Date of Purchase", validators=[DataRequired()])
    dateuse = DateField("Date of 1st Use", validators=[DataRequired()])
