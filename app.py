import os
from tqdm import tqdm
from pprint import pprint

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from routes import Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Helper():
    def __init__(self):
        if  not os.path.isfile('./records.db'):
            self.create_database()

        api.add_resource(Image, '/image')
        
    def create_database(self):
        with app.app_context():
            db.create_all()

    def insert_fake_users(self):
        admin = User(username='admin', email='admin@example.com')
        guest = User(username='guest', email='guest@example.com')
        with app.app_context():
            db.session.add(admin)
            db.session.add(guest)
            db.session.commit()

    def delete_fake_users(self):
        with app.app_context():
            query_users = User.query.all()
            for user in query_users:
                db.session.delete(user)
            db.session.commit()


    def print_all_rows(self):
        with app.app_context():
            print(User.query.all())



if __name__ == "__main__":
    helper = Helper()
    # helper.print_all_rows()
    app.run(debug=True)