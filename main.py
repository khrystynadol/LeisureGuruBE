from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
# from database.models import User

DB_NAME = "database.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

# Initialize the db
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(150), unique=True)
    password1 = db.Column(db.String(150))
    password2 = db.Column(db.String(150))
    confirm_pw = db.Column(db.Boolean, default=False)
    verification = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=False)


@app.route("/")
def home():
    return "Home page :)"


@app.route("/api/v1/hello-world-<value>")
def hello_world(value):
    return "Hello world " + value, 200


@app.route("/test", methods=['POST', 'GET'])
def test():
    title = "Add data testing..."
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        new_user = User(first_name=first_name, last_name=last_name, email=email,
                        password1=password1, password2=password2)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
    return render_template("test.html", title=title)


def create_database(dbapp):
    if not path.exists("/database/" + DB_NAME):
        db.create_all(app=dbapp)
        print('Created Database!')


if __name__ == "__main__":
    create_database(app)
    app.run()
