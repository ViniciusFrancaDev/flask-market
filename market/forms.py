from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please, try a different username"
            )

    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError(
                "Email address already exists! Please, try a different email address"
            )

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
