from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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


@app.route("/test", methods=['POST', 'GET'])
def test():
    title = "Add data testing..."
    if request.method == 'POST':
        if request.is_json:
            data_user = request.get_json()
            new_user = User(first_name=data_user['first_name'], last_name=data_user['last_name'],
                            email=data_user['email'],
                            password1=data_user['password1'], password2=data_user['password2'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.first_name} {new_user.last_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    return render_template("test.html", title=title)


if __name__ == "__main__":
    app.run()
