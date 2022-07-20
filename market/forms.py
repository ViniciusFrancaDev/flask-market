from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField(
        label="User Name:", validators=[Length(min=2, max=30), DataRequired()]
    )
    email_address = StringField(
        label="Email Address:", validators=[Email(), DataRequired()]
    )
    password = PasswordField(
        label="Password:", validators=[Length(min=6), DataRequired()]
    )
    password_confirmation = PasswordField(
        label="Confirm Password:", validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")
