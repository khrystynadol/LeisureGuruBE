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
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:pass1234@localhost:5432/{DB_NAME}'

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


@auth.verify_password
def verify_password(email, password):
    print("email: " + email + ", password: " + password)
    user_to_verify = User.query.filter_by(email=email).first()
    if user_to_verify is not None and check_password_hash(user_to_verify.password, password):
        print("email: " + email + ", password: " + password)
        return user_to_verify
    else:
        return False


@auth.error_handler
def auth_error_handler(status):
    message = ""
    if status == 401:
        message = "Wrong email or password"
    if status == 403:
        message = "Access denied"
    return {"code": status, "message": message}, status


def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'
    return resp


# def login_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth_b = request.authorization
#         if not auth_b or not verify_password(auth_b.email, auth_b.password):
#             return authenticate()
#         return f(*args, **kwargs)
#     return decorated


def send_mes(to, subject, url):
    msg = Message(subject, sender='leisure.guru.ver@gmail.com', recipients=[to])
    msg.body = f"Please confirm email: {url}"
    mail.send(msg)


@app.route('/rest-auth')
@auth.login_required
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


# @app.route("/register", methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         if request.is_json:
#             data_user = request.get_json()
#             new_user = User(first_name=data_user['firstName'], last_name=data_user['lastName'],
#                             email=data_user['email'], birth_date=data_user['date'],
#                             password=generate_password_hash(data_user['password']))
#             find_email = User.query.filter_by(email=new_user.email).first()
#
#             if find_email is not None:
#                 flash("Email is already used", "error")
#                 abort(400)
#             elif not re.match(r'[^@]+@[^@]+\.[^@]+', new_user.email):
#                 flash("Incorrect email")
#                 abort(400)
#             elif not re.match(r'[A-Za-z]+', new_user.first_name):
#                 flash("Incorrect first name")
#                 abort(400)
#             elif not re.match(r'[A-Za-z]+', new_user.last_name):
#                 flash("Incorrect last name")
#                 abort(400)
#             elif not new_user.first_name or not new_user.last_name or not new_user.password or not new_user.email \
#                     or not new_user.birth_date:
#                 flash("All fields should be entered")
#                 abort(400)
#             else:
#                 db.session.add(new_user)
#                 db.session.commit()
#                 return {"id": new_user.id,
#                         "email": new_user.email}
#         else:
#             return {"code": 400,
#                     "message": "Not json format"}, 400
#     else:
#         return "Sign up :)"

@app.route('/confirm')
def confirm():
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
    return redirect(url_for('confirm'))  # return "Confirm email"  # redirect(url_for('main.home'))


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
@error_handler
def registration():
    if request.method == 'POST' and request.is_json:
        user_data = UserSchema().load(request.json)
        user_data["photo"] = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png"
        new_user = User(**user_data)
        find_email = User.query.filter_by(email=new_user.email).first()
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
                return {"id": user_login.id,
                        "email": user_login.email}, 200
            else:
                return {
                    "code": 408,
                    "message": "You need to authorize!"
                }, 408
    else:
        return {"code": 404,
                "message": "Incorrect request"}, 404


@app.route("/profile/logout/<int:user_id>", methods=['GET'])
@auth.login_required
def logout(user_id):
    user_to_work = User.query.filter_by(id=user_id).first()
    current_user = auth.current_user()
    print(user_id, current_user.id)
    if current_user.id != int(user_id):
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
@auth.login_required
def user(user_id):
    user_to_work = User.query.filter_by(id=user_id).first()
    current_user = auth.current_user()
    print(user_id, current_user.id)
    if current_user.id != int(user_id):
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
@auth.login_required
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
@auth.login_required
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
@auth.login_required
def place(place_id):
    place_to_work = Place.query.filter_by(id=place_id).all()
    # user_to_work_data = request.get_json()
    if request.method == 'GET' and place_to_work != []:
        return json.dumps([p.format() for p in place_to_work]), 200


@app.route("/place/photos/<int:place_id>", methods=['GET'])
@auth.login_required
def place_photo(place_id):
    place_to_work = Place.query.filter_by(id=place_id).all()
    # user_to_work_data = request.get_json()
    if request.method == 'GET' and place_to_work != []:
        return json.dumps([p.format() for p in PlacePhoto.query.filter_by(place_id=place_id).all()]), 200


if __name__ == "__main__":
    app.run()
