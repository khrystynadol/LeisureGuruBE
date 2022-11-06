from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from wtforms import Form, BooleanField, StringField, PasswordField, DateField, EmailField, validators

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)

DB_NAME = 'LeisureGuru'

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost:5432/{DB_NAME}'
app.debug = True


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password1 = db.Column(db.String(200), nullable=False)
    verification = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User: '{}' '{}', email: '{}'>" \
            .format(self.first_name, self.last_name, self.email)

    def is_authenticated(self) -> bool:
        return True

    def is_active(self) -> bool:
        return True

    def is_anonymous(self) -> bool:
        return False

    def get_id(self):
        return self.id


class Activity(db.Model):
    __tablename__ = 'activity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Season(db.Model):
    __tablename__ = 'season'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)


class Place(db.Model):
    __tablename__ = 'place'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(25), nullable=True)
    # street = db.Column(db.String(50), nullable=False)
    # house = db.Column(db.Integer, nullable=False)
    # flat = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(1000), nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(250), nullable=False)
    visible = db.Column(db.Boolean, default=False)


class PlaceActivity(db.Model):
    __tablename__ = 'place_activity'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))


class PlaceSeason(db.Model):
    __tablename__ = 'place_season'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'))


class RegistrationForm(Form):
    first_name = StringField('First name', [validators.DataRequired("Please enter your first name."),
                                            validators.Length(min=1, max=50)])
    last_name = StringField('Last name', [validators.DataRequired("Please enter your last name."),
                                          validators.Length(min=1, max=50)])
    birth_date = DateField('Date of birth', [validators.DataRequired("Please enter your birth date.")],
                           format='%d/%m/%Y')
    email = EmailField('Email', [validators.DataRequired("Please enter your email address."),
                                 validators.Email("This field requires a valid email address")])
    password1 = PasswordField('Password', [
        validators.DataRequired("Please enter your password."),
        validators.EqualTo('password2', message='Password must match')
    ])
    password2 = PasswordField("Please confirm your password")


# class Event(db.Model):
#     __tablename__ = 'event'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(1000), nullable=False)
#     date_time = db.Column(db.DateTime, nullable=False)
#     rate = db.Column(db.Integer, nullable=False)
#     image = db.Column(db.String(250), nullable=False)
#     place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
