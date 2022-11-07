from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, DateField, EmailField, validators


class RegistrationForm(FlaskForm):
    first_name = StringField('First name', [validators.DataRequired("Please enter your first name."),
                                            validators.Length(min=1, max=50)])
    last_name = StringField('Last name', [validators.DataRequired("Please enter your last name."),
                                          validators.Length(min=1, max=50)])
    birth_date = DateField('Date of birth', [validators.DataRequired("Please enter your birth date.")],
                           format='%Y-%m-%d')
    email = EmailField('Email', [validators.DataRequired("Please enter your email address."),
                                 validators.Email("This field requires a valid email address")])
    password = PasswordField('Password', [validators.DataRequired("Please enter your password.")])
