from flask import request, flash, abort, render_template, url_for
from flask_login import login_required, current_user, login_user, logout_user, LoginManager  # , UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail
import re
<<<<<<< Updated upstream
import os
from token import generate_confirmation_token, confirm_token
from email import send_email
from database.models import app, db, User, Place, RegistrationForm
=======
import json
from token import generate_confirmation_token, confirm_token
from forms import UserSchema
from database.models import *
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
>>>>>>> Stashed changes

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

<<<<<<< Updated upstream
mail = Mail(app)

=======
app.config['SECRET_KEY'] = 'super secret key'
app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']
>>>>>>> Stashed changes
# mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# gmail authentication
app.config['MAIL_USERNAME'] = 'leisure.guru.ver@gmail.com'
app.config['MAIL_PASSWORD'] = 'innsblomcwfddjgw'

# mail accounts
<<<<<<< Updated upstream
# MAIL_DEFAULT_SENDER = 'from@example.com'
=======
app.config['MAIL_DEFAULT_SENDER'] = 'leisure.guru.ver@gmail.com'

mail = Mail(app)

def send_mes(to,subject, url):
    msg = Message(subject,sender='leisure.guru.ver@gmail.com',recipients=[to])
    msg.body = f"Please confirm email: {url}"
    mail.send(msg)



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
>>>>>>> Stashed changes


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def load_all_places():
    return Place.query.all()


@app.route("/")
def home():
    return "Home page :)"


<<<<<<< Updated upstream
# @app.route("/signup", methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         if request.is_json:
#             data_user = request.get_json()
#             new_user = User(first_name=data_user['firstName'], last_name=data_user['lastName'],
#                             email=data_user['email'], birth_date=data_user['date'],
#                             password1=generate_password_hash(data_user['password']))
#             find_email = User.query.filter_by(email=new_user.email).first()
#
#             if find_email is not None:
#                 flash("Email is already used")
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
#             elif not new_user.first_name or not new_user.last_name or not new_user.password1 or not new_user.email \
#                     or not new_user.birth_date:
#                 flash("All fields should be entered")
#                 abort(400)
#             else:
#                 db.session.add(new_user)
#                 db.session.commit()
#                 return {"id": new_user.id,
#                         "email": new_user.email}
#         else:
#             abort(400)
#     return "Sign up :)"


=======
>>>>>>> Stashed changes
@app.route('/confirm/<token>')
#@login_required
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


<<<<<<< Updated upstream
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            form = RegistrationForm(request.form)
            if form.validate_on_submit():
                new_user = User(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    birth_date=form.birth_date.data,
                    password1=generate_password_hash(form.password1.data)
                )
                find_email = User.query.filter_by(email=user.email).first()
                if find_email is not None:
                    flash("Email is already used", "error")
                else:
                    db.session.add(user)
                    db.session.commit()
                    return {"id": new_user.id,
                            "email": new_user.email}

                token = generate_confirmation_token(new_user.email)
                confirm_url = url_for('new_user.confirm_email', token=token, _external=True)
                html = render_template('activate.html', confirm_url=confirm_url)
                subject = "Please confirm your email"
                send_email(new_user.email, subject, html)

                login_user(new_user)

                flash('A confirmation email has been sent via email.', 'success')
            return "Home"  # redirect(url_for("main.home"))
=======
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST' and request.is_json:
        user_data = UserSchema().load(request.json)
        new_user = User(**user_data)
        find_email = User.query.filter_by(email=new_user.email).first()
        if find_email is not None:
            flash("Email is already used", "error")
        else:
            db.session.add(new_user)
            db.session.commit()
            print({"id": new_user.id,
                    "email": new_user.email})

            token = generate_confirmation_token(new_user.email)
            confirm_url = url_for('confirm_email', token=token, _external=True)
            #html = render_template('activate.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            send_mes(new_user.email,subject, confirm_url)
        #send_emailqwert(new_user.email, subject, html)
        login_user(new_user)

        flash('A confirmation email has been sent via email.', 'success')
        return "Home"
>>>>>>> Stashed changes
    return "Register"  # render_template('/register', form=form)


@app.route("/login", methods=['PUT', 'GET'])
def login():
    if request.method == 'PUT':
        login_data = request.get_json()
        user_login = User.query.filter_by(email=login_data['email']).first()

        if user_login is None:
            abort(400)
        elif not check_password_hash(user_login.password1, login_data['password']):
            abort(400)
        else:
            user_login.status = True
            login_user(user_login)
            db.session.commit()
            return {"id": user_login.id,
                    "email": user_login.email}
    return "Login :)"


@app.route("/user/<int:user_id>", methods=['GET', 'DELETE', 'POST'])
@login_required
def user(user_id):
    user_to_work = User.query.get_or_404(user_id)
    if request.method == 'GET':
        user_to_work.status = False
        # db.session.add(user_to_work)
        db.session.commit()
        logout_user()
        # db.session.pop('id', None)
        # db.session.pop('email', None)
    elif request.method == 'DELETE':
        if user_id == current_user.id:
            db.session.delete(user_to_work)
            db.session.commit()
            flash("Success")
        else:
            flash("You try to delete other user")
            abort(404)
    return "User"


@app.route("/place", methods=['GET'])
@login_required
def place():
    if request.method == 'GET':
        places = load_all_places()
        # we need to remake it to work with FE correctly
        return {
            places
        }
    return "Place"


if __name__ == "__main__":
    app.run()
