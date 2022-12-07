from database.models import db
import datetime
from marshmallow import Schema, fields, validate, validates, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash


class UserSchema(Schema):
    id = fields.Integer(validate=validate.Range(min=0))
    first_name = fields.Str(validate=[validate.Regexp("[a-zA-z]*$"),
                            validate.Length(min=0, max=45)],
                            required=True)
    last_name = fields.Str(validate=[validate.Regexp("[a-zA-z]*$"),
                           validate.Length(min=0, max=45)],
                           required=True)
    email = fields.Email(unique=True, required=True)
    birth_date = fields.Date(format='%Y-%m-%d',
                             validate=lambda x: x <= datetime.date.today(),
                             required=True)
    password = fields.Function(  # validate=validate.Length(min=5, max=15),
                               deserialize=lambda password: generate_password_hash(password),
                               load_only=True, required=True)
    photo = fields.Str(validate=validate.Length(min=0, max=500), required=False)
    verification = fields.Boolean(required=False)


class PlaceSchema(Schema):
    id = fields.Integer(validate=validate.Range(min=0))
