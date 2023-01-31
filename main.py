import requests
from flask import request, flash, jsonify, url_for, make_response, redirect
from werkzeug.security import check_password_hash
from flask_mail import Message
from flask_mail import Mail
import psycopg2
import json
from generate_token import generate_confirmation_token, confirm_token
from forms import UserSchema
from database.models import *
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity)


# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost:5432/{DB_NAME}'

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_SECRET_KEY"] = "super-secret-vnjfvnerjhnavcjienanreugvneivnkj"  # Change this!
jwt = JWTManager(app)

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


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/token", methods=["PUT"])
def create_token():
    user_email = request.json.get("email", None)
    password = request.json.get("password", None)
    user_to_verify = User.query.filter_by(email=user_email).first()
    if user_to_verify is not None and check_password_hash(user_to_verify.password, password):
        # access_token = create_access_token(identity=user_email)
        return {'access_token': create_access_token(identity=user_email, additional_claims={'user_id': user_to_verify.id}),
                'refresh_token': create_refresh_token(identity=user_email)}
    else:
        return {"code": 401, "message": "Bad email or password"}, 401


@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    return {'access_token': create_access_token(identity=current_user)}, 200


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


def verify_password(email, password):
    user_to_verify = User.query.filter_by(email=email).first()
    if user_to_verify is not None and check_password_hash(user_to_verify.password, password):
        print("email: " + email + ", password: " + password)
        return user_to_verify
    else:
        return False


def send_mes(to, subject, url):
    msg = Message(subject, sender='leisure.guru.ver@gmail.com', recipients=[to])
    msg.body = f"Please confirm email: {url}"
    mail.send(msg)


@app.route('/rest-auth')
@jwt_required()
def get_response():
    return {'code': 200,
            'message': 'You are authorized.'}, 200


def error_handler(func):
    def wrapper(*args, **kwargs):
        # print("error_handler")
        try:
            # result = 0
            if 0 == len(kwargs):
                result = func()
            else:
                result = func(**kwargs)
            if result.__class__ == tuple and result[1] >= 400:
                return {
                    "code": result[1],
                    "message": result[0]
                }, result[1]
            else:
                return result
        except ValidationError as err:
            # print(err.messages)
            return {"code": 412,
                    "message": str(
                        err.messages_dict).replace('{', '').replace('}', '').replace('[', '').replace(']', '')
                    }, 412
        except IntegrityError as err:
            # print(err.args)
            return {"code": 409,
                    "message": "Email is not unique"
                    }, 409

    wrapper.__name__ = func.__name__
    return wrapper


@app.route("/")
def home():
    return "Home page :)"


@app.route('/confirm', methods=['GET'])
def confirm():
    if request.method == 'GET':
        response = make_response()
        response.status_code = 200
        return response


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
    return redirect(url_for('confirm'))
    # return "Confirm email"  # redirect(url_for('main.home'))


@app.route('/registration', methods=['GET', 'POST'])
@error_handler
def registration():
    if request.method == 'POST' and request.is_json:
        user_data = UserSchema().load(request.json)
        user_data["photo"] = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png"
        new_user = User(**user_data)
        # find_email = User.query.filter_by(email=new_user.email).first()
        db.session.add(new_user)
        db.session.commit()

        token = generate_confirmation_token(new_user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        # html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_mes(new_user.email, subject, confirm_url)
        # return {"id": new_user.id,
        #         "email": new_user.email}, 201
        return {'access_token': create_access_token(identity=new_user.email,
                                                    additional_claims={'user_id': new_user.id}),
                'refresh_token': create_refresh_token(identity=new_user.email)}
    else:
        return {
            "code": 404,
            "message": "Incorrect request"
        }, 404  # render_template('/register', form=form)


@app.route("/login", methods=['PUT', 'GET'])
def login():
    if request.method == 'PUT':
        login_data = request.get_json()
        user_login = User.query.filter_by(email=login_data['email']).first()
        if user_login is None:
            return {
                       "code": 404,
                       "message": "User not found"
                   }, 404
        elif not check_password_hash(user_login.password, login_data['password']):
            return {
                       "code": 404,
                       "message": "Incorrect password"
                   }, 404
        else:
            if verify_password(login_data['email'], login_data['password']):
                user_login.status = True
                db.session.commit()
                app.config['USERNAME'] = login_data['email']
                app.config['PASSWORD'] = login_data['password']
                # return {"id": user_login.id,
                #         "email": user_login.email}, 200
                return {'access_token': create_access_token(identity=user_login.email,
                                                            additional_claims={'user_id': user_login.id}),
                        'refresh_token': create_refresh_token(identity=user_login.email)}
            else:
                return {
                    "code": 408,
                    "message": "You need to authorize!"
                }, 408
    else:
        return {"code": 404,
                "message": "Incorrect request"}, 404


@app.route("/profile/logout/<int:user_id>", methods=['GET'])
@jwt_required()
def logout(user_id):
    user_to_work = User.query.filter_by(id=user_id).first()
    current_user = get_jwt_identity()
    print(user_id, current_user)
    if user_to_work.email != current_user:
        return {"code": 403,
                "message": "Access denied"}, 403

    if request.method == 'GET' and user_to_work != []:
        print("Got", user_id)
        user_to_work.status = False
        # db.session.add(user_to_work)
        db.session.commit()
        # db.session.pop('id', None)
        # db.session.pop('email', None)
        response = make_response()
        response.status_code = 200
        return response
    else:
        return {"code": 404,
                "message": "Incorrect request"}, 404


@app.route("/profile/<int:user_id>", methods=['GET', 'DELETE', 'POST', 'PUT'])
@jwt_required()
def user(user_id):
    user_to_work = User.query.filter_by(id=user_id).first()
    current_user = get_jwt_identity()
    print(user_id, current_user)
    if user_to_work.email != current_user:
        return {"code": 403,
                "message": "Access denied"}, 403

    # user_to_work_data = request.get_json()
    if request.method == 'GET' and user_to_work != []:
        return jsonify(UserSchema().dump(user_to_work)), 200
    elif request.method == 'DELETE' and user_to_work != []:
        print("Got delete 1", user_id)
        db.session.delete(user_to_work)
        db.session.commit()
        response = make_response()
        response.status_code = 200
        return response
    else:
        return {"code": 404,
                "message": "Incorrect request"}, 404


@app.route("/homepage", methods=['GET'])
def homepage():
    return json.dumps([p.as_dict() for p in Place.query.all()]), 200


@app.route("/activities", methods=['GET'])
def activities():
    if request.method == 'GET':
        return json.dumps([p.as_dict() for p in Activity.query.all()]), 200


@app.route("/filter", methods=['POST'])
@jwt_required()
def filtering():
    if request.method == 'POST':
        filter_data = request.get_json()
        rate_filter = []
        if "rate" in filter_data and filter_data["rate"] != []:
            rate_filter.append(filter_data["rate"])
            min_rate = filter_data["rate"]
            for i in range(1, 6):
                if i > min_rate:
                    rate_filter.append(i)
        else:
            rate_filter = [1, 2, 3, 4, 5]
        # print("rate_filter", rate_filter)

        activity_filter = []
        if "activities" in filter_data and filter_data["activities"] != []:
            activity_filter = filter_data["activities"]
        else:
            activity_filter = (p.get_id() for p in Activity.query.all())

        # place_filter_by_activity = (p.get_id() for p in
        #                             PlaceActivity.query.filter(PlaceActivity.activity_id.in_(activity_filter)))
        place_filter_res = (p.get_place_id() for p in
                            PlaceActivity.query.filter(PlaceActivity.activity_id.in_(activity_filter)))

        # print("activity_filter", activity_filter)
        # print("place_filter_by_activity:", place_filter_by_activity)
        # filter1 = filter_data["id"]
        if "search_box" in filter_data:
            conn = psycopg2.connect(
                database=DB_NAME,
                user='postgres',
                password='pass1234',
                host='localhost',
                port='5432'
            )
            cursor = conn.cursor()
            search_filter = filter_data["search_box"]
            search_filter_1 = (filter_data["search_box"]).lower().capitalize()
            search_filter_2 = (filter_data["search_box"]).upper()
            search_filter_3 = (filter_data["search_box"]).lower()
            like_pattern = '%{}%'.format(search_filter)
            like_pattern_1 = '%{}%'.format(search_filter_1)
            like_pattern_2 = '%{}%'.format(search_filter_2)
            like_pattern_3 = '%{}%'.format(search_filter_3)
            cursor.execute('SELECT id FROM place '
                           'WHERE (place.name LIKE (%s) OR place.name LIKE (%s) '
                           'OR place.name LIKE (%s) OR place.name LIKE (%s) '
                           'OR place.city LIKE (%s) OR place.city LIKE (%s) '
                           'OR place.city LIKE (%s) OR place.city LIKE (%s) '
                           'OR place.country LIKE (%s) OR place.country LIKE (%s) '
                           'OR place.country LIKE (%s) OR place.country LIKE (%s));',
                           (like_pattern, like_pattern_1, like_pattern_2, like_pattern_3,
                            like_pattern, like_pattern_1, like_pattern_2, like_pattern_3,
                            like_pattern, like_pattern_1, like_pattern_2, like_pattern_3))
            cursor_res = [p[0] for p in cursor.fetchall()]
            places = []
            for id in cursor_res:
                places.append(Place.query.filter_by(id=id).first())
            # search_res = json.dumps([p.format() for p in places])
            # Closing the connection
            conn.close()
            return json.dumps([p.format() for p in places]), 200
        else:
            all_filter = Place.query.filter(Place.id.in_(place_filter_res),
                                            Place.rate.in_(rate_filter))
        return json.dumps([p.format() for p in all_filter]), 200


@app.route("/trial", methods=['POST'])
@jwt_required()
def trial():
    if request.method == 'POST':
        # filter_data = request.get_json()
        # search_filter = filter_data["search_box"]
        # search_filter_1 = (filter_data["search_box"]).lower().capitalize()
        # all_filter = Place.query.filter(Place.id.in_(place_filter_res),
        #                                 Place.rate.in_(rate_filter),
        #                                 Place.name.like(f"%{search_filter}%"))
        return "Success", 200
    # Closing the connection
    # conn.close()


@app.route("/place/<int:place_id>", methods=['GET'])
@jwt_required()
def place(place_id):
    place_to_work = Place.query.filter_by(id=place_id).all()
    # user_to_work_data = request.get_json()
    if request.method == 'GET' and place_to_work != []:
        return json.dumps([p.format() for p in place_to_work]), 200


@app.route("/place/photos/<int:place_id>", methods=['GET'])
@jwt_required()
def place_photo(place_id):
    place_to_work = Place.query.filter_by(id=place_id).all()
    # user_to_work_data = request.get_json()
    if request.method == 'GET' and place_to_work != []:
        return json.dumps([p.format() for p in PlacePhoto.query.filter_by(place_id=place_id).all()]), 200


@app.route('/weather', methods=['GET'])
def weather():
    city_data = request.get_json()
    city = city_data["city"]
    api_key = "d081fd79869e33def9f03881614a21da"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    weather_data = requests.get(url).json()
    # print(jsonify(weather_data))
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run()
