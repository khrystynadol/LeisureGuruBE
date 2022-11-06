from flask import request, flash, abort
from flask_login import login_required, current_user, login_user, logout_user, LoginManager  # , UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import re
from database.models import app, db, User, Place

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# mail settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# gmail authentication
MAIL_USERNAME = os.environ['leisure.guru.ver@gmail.com']
MAIL_PASSWORD = os.environ['LeisureGuru12345']

# mail accounts
#MAIL_DEFAULT_SENDER = 'from@example.com'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def load_all_places():
    return Place.query.all()


@app.route("/")
def home():
    return "Home page :)"


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


@app.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('main.home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(
            first=form.first_name.data,
            last=form.last_name.data,
            birth=form.birth_date.data,
            email=form.email.data,
            password1=form.password1.data,
            password2=form.password2.data
        )
        find_email = User.query.filter_by(email=user.email).first()
        if find_email is not None:
            flash('Email is alredy used')
        else:
            db.session.add(user)
            db.session.commit()
            return {"id": new_user.id,
                    "email": new_user.email}

        token = generate_confirmation_token(user.email)
        confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("main.home"))

    return render_template('user/register.html', form=form)

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
