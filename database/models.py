from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)

DB_NAME = 'LeisureGuru'

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:pass1234@localhost:5432/{DB_NAME}'
app.debug = True


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(500), nullable=False)
    verification = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User: '{}' '{}', email: '{}'>" \
            .format(self.first_name, self.last_name, self.email)

    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}

    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            # 'birth_date': self.birth_date,
            'email': self.email,
        }

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

    def get_id(self):
        return self.id

    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}


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
    description = db.Column(db.String(2000), nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(500), nullable=False)
    visible = db.Column(db.Boolean, default=False)

    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'city': self.city,
            'description': self.description,
            'rate': self.rate,
            'image': self.image
        }

    def get_id(self):
        return self.id


class PlacePhoto(db.Model):
    __tablename__ = 'place_photo'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(1000), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))

    def format(self):
        return {
            'image': self.image
        }

    def as_dict(self):
        return {p.image: getattr(self, p.image) for p in self.__table__.columns}


class PlaceActivity(db.Model):
    __tablename__ = 'place_activity'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

    def get_place_id(self):
        return self.place_id

    def get_id(self):
        return self.id


class PlaceSeason(db.Model):
    __tablename__ = 'place_season'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'))


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
