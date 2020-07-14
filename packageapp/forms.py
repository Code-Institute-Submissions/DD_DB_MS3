from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms import DateField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email
from wtforms.validators import Length, EqualTo, NumberRange


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
    brand = StringField("Brand", validators=[Length(max=30)])
    capacity = IntegerField("Capacity (ml/gr) *",
                            validators=[InputRequired(),
                                        NumberRange(min=1, max=3000)])
    dueperiod = IntegerField("Due in (nº months)",
                             validators=[NumberRange(min=1, max=12)])
