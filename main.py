from flask import Flask, render_template, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_NAME = 'LeisureGuru'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost:5432/{DB_NAME}'
app.debug = True


# Initialize the db
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(50), unique=True)
    password1 = db.Column(db.String(50))
    password2 = db.Column(db.String(50))
    confirm_pw = db.Column(db.Boolean, default=False)
    verification = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User: '{}' '{}', email: '{}'>" \
            .format(self.first_name, self.last_name, self.email)


@app.route("/")
def home():
    return "Home page :)"


@app.route("/api/v1/hello-world-<value>")
def hello_world(value):
    return "Hello world " + value, 200


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        if request.is_json:
            data_user = request.get_json()
            new_user = User(first_name=data_user['firstName'], last_name=data_user['lastName'],
                            email=data_user['email'], birth_date=data_user['date'],
                            password1=data_user['password'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.first_name} {new_user.last_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    return "Sign up :)"


@app.route("/delete/<int:user_id>", methods=['GET', 'DELETE'])
# @login_required
def delete(user_id):
    if user_id == current_user.id:
        user_to_delete = User.query.filter_by(id=user_id).first()
        if request.method == 'DELETE':
            db.session.delete(user_to_delete)
            db.session.commit()
            flash("Success")
        abort(404)
    else:
        flash("You try to delete other user")
    return "Delete user"


if __name__ == "__main__":
    app.run()
