from flask import request, flash, abort, jsonify, render_template, url_for
# from flask_login import login_required, current_user, login_user, logout_user, LoginManager  # , UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message
from flask_mail import Mail

import re
import json
import os
from generate_token import generate_confirmation_token, confirm_token
# from check_email import send_email
from forms import UserSchema
from database.models import *
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost:5432/{DB_NAME}'

'''
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
'''

app.config['SECRET_KEY'] = 'super secret key'
app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']
# mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# gmail authentication
app.config['MAIL_USERNAME'] = 'leisure.guru.ver@gmail.com'
app.config['MAIL_PASSWORD'] = 'innsblomcwfddjgw'

# mail accounts
app.config['MAIL_DEFAULT_SENDER'] = 'leisure.guru.ver@gmail.com'

mail = Mail(app)


def send_mes(to, subject, url):
    msg = Message(subject, sender='leisure.guru.ver@gmail.com', recipients=[to])
    msg.body = f"Please confirm email: {url}"
    mail.send(msg)


@app.route('/rest-auth')
@auth.login_required
def get_response():
    return jsonify('You are authorized.')


def error_handler(func):
    def wrapper(*args, **kwargs):
        # print("error_handler")
        try:
            # result = 0
            if 0 == len(kwargs):
                result = func()
            else:
                result = func(**kwargs)
            if result[1] >= 400:
                return {
                    "code": result[1],
                    "message": result[0]
                }, result[1]
            else:
                return result
        except ValidationError as err:
            # print(err.messages)
            return {"code": 412,
                    "message": err.messages
                    }, 412
        except IntegrityError as err:
            # print(err.args)
            return {"code": 409,
                    "message": err.args
                    }, 409

    wrapper.__name__ = func.__name__
    return wrapper


'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def load_all_places():
    return Place.query.all()
'''


@app.route("/")
def home():
    return "Home page :)"


@app.route("/register", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        if request.is_json:
            data_user = request.get_json()
            new_user = User(first_name=data_user['firstName'], last_name=data_user['lastName'],
                            email=data_user['email'], birth_date=data_user['date'],
                            password1=generate_password_hash(data_user['password']))
            find_email = User.query.filter_by(email=new_user.email).first()

            if find_email is not None:
                flash("Email is already used", "error")
                abort(400)
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', new_user.email):
                flash("Incorrect email")
                abort(400)
            elif not re.match(r'[A-Za-z]+', new_user.first_name):
                flash("Incorrect first name")
                abort(400)
            elif not re.match(r'[A-Za-z]+', new_user.last_name):
                flash("Incorrect last name")
                abort(400)
            elif not new_user.first_name or not new_user.last_name or not new_user.password1 or not new_user.email \
                    or not new_user.birth_date:
                flash("All fields should be entered")
                abort(400)
            else:
                db.session.add(new_user)
                db.session.commit()
                return {"id": new_user.id,
                        "email": new_user.email}
        else:
            abort(400)
    return "Sign up :)"


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email_to_check = confirm_token(token)
    finally:
        flash('The confirmation link is invalid or has expired.', 'danger')

    user_to_check = User.query.filter_by(email=email_to_check).first_or_404()
    if user_to_check.verification:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user_to_check.verification = True
        db.session.add(user_to_check)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return "Confirm email"  # redirect(url_for('main.home'))


'''
@app.route('/registration', methods=['GET', 'POST'])
@error_handler
def registration():
    if request.method == 'POST' and request.is_json:
        data_user = UserSchema().load(request.json)
        new_user = User(**data_user)
        new_user.status = True
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id,
                "email": new_user.email}, 201
        # jsonify(UserSchema().dump(new_user)), 201
    return "Register"  # render_template('/register', form=form)
'''


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST' and request.is_json:
        user_data = UserSchema().load(request.json)
        new_user = User(**user_data)
        find_email = User.query.filter_by(email=new_user.email).first()
        if find_email is not None:
            return {"message": "Email already exists."}, 405
        else:
            db.session.add(new_user)
            db.session.commit()

            token = generate_confirmation_token(new_user.email)
            confirm_url = url_for('confirm_email', token=token, _external=True)
            # html = render_template('activate.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            send_mes(new_user.email, subject, confirm_url)
            # send_emailqwert(new_user.email, subject, html)
        # flash('A confirmation email has been sent via email.', 'success')
        return {"id": new_user.id,
                "email": new_user.email}, 201
    else:
        return {
            "message": "Incorrect request"
        }, 404  # render_template('/register', form=form)


@app.route("/login", methods=['PUT', 'GET'])
def login():
    if request.method == 'PUT':
        login_data = request.get_json()
        user_login = User.query.filter_by(email=login_data['email']).first()

        if user_login is None:
            abort(405)
        elif not check_password_hash(user_login.password1, login_data['password']):
            abort(405)
        else:
            user_login.status = True
            db.session.commit()
            return {"id": user_login.id,
                    "email": user_login.email}
    return "Login :)"


@app.route("/profile/<int:user_id>", methods=['GET', 'DELETE', 'POST', 'PUT'])
# @auth.login_required
def user(user_id):
    # user_to_work_data = request.get_json()
    user_to_work = User.query.filter_by(id=user_id).first()
    if request.method == 'GET' and user_to_work != []:
        print("Got", user_id)
        user_to_work.status = False
        # db.session.add(user_to_work)
        db.session.commit()
        # db.session.pop('id', None)
        # db.session.pop('email', None)
    elif request.method == 'DELETE' and user_to_work != []:
        print("Got delete 1", user_id)
        if user_to_work.id == auth.current_user().id:
            db.session.delete(user_to_work)
            db.session.commit()
            print("Got delete 2", user_id)
            flash("Success")
        else:
            flash("You try to delete other user")
            abort(404)
    return "User"


@app.route("/homepage", methods=['GET'])
# @login_required
def homepage():
    return json.dumps([p.as_dict() for p in Place.query.all()])


@app.route("/filter", methods=['GET'])
def filtering():
    if request.method == 'GET':
        filter_data = request.get_json()
        rate_filter = []
        if "rate" in filter_data:
            rate_filter.append(filter_data["rate"])
        else:
            rate_filter = [1, 2, 3, 4, 5]
        # print("rate_filter", rate_filter)

        activity_filter = []
        if "activities" in filter_data:
            activity_filter_list = filter_data["activities"]
            # print(activity_filter_list)
            activity_filter = (p.get_id() for p in Activity.query.filter(Activity.name.in_(activity_filter_list)))
        else:
            activity_filter = (p.get_id() for p in Activity.query.all())

        # print("activity_filter", activity_filter)
        place_filter_by_activity = (p.get_place_id() for p
                                    in PlaceActivity.query.filter(PlaceActivity.activity_id.in_(activity_filter)))
        # print("place_filter_by_activity:", place_filter_by_activity)
        # filter1 = filter_data["id"]
        if "search_box" in filter_data:
            search_filter = filter_data["search_box"]
            all_filter = Place.query.filter(Place.id.in_(place_filter_by_activity),
                                            Place.rate.in_(rate_filter),
                                            Place.name.like(f"%{search_filter}%"))
        else:
            all_filter = Place.query.filter(Place.id.in_(place_filter_by_activity),
                                            Place.rate.in_(rate_filter))
        return json.dumps([p.format() for p in all_filter]), 201


if __name__ == "__main__":
    app.run()
