from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = 'Lorem ipsum dolor sit amet.'
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(myapp)

    from LeisureGuruBE.home import home_page
    myapp.register_blueprint(home_page, url_prefix='/')

    create_database(myapp)

    return myapp


def create_database(myapp):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=myapp)
        print('Created Database!')


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
