from flask import Flask, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import login_required, current_user, login_user, logout_user, LoginManager  # , UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)

DB_NAME = 'LeisureGuru'

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost:5432/{DB_NAME}'
app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(50), unique=True)
    password1 = db.Column(db.String(200))
    password2 = db.Column(db.String(200))
    confirm_pw = db.Column(db.Boolean, default=False)
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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return "Home page :)"


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        if request.is_json:
            data_user = request.get_json()
            new_user = User(first_name=data_user['firstName'], last_name=data_user['lastName'],
                            email=data_user['email'], birth_date=data_user['date'],
                            password1=generate_password_hash(data_user['password']))
            find_email = User.query.filter_by(email=new_user.email).first()

            if find_email is not None:
                flash("Email is already used")
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


if __name__ == "__main__":
    app.run()
