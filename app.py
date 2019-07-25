import os
import pandas as pd
from tqdm import tqdm
from pprint import pprint

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

# from routes import Image, Login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SqlAlchemy
db = SQLAlchemy()
db.init_app(app)
# Setting up Flask-RESTFUL Api
api = Api(app)

class Image(Resource):
    def get(self):
        return random.choice(dataset['path'])

class Login(Resource):
    def get(self):
        return "Do not try to get Login"

    def post(self):
        json_data = request.get_json(force=True)
        # pprint(json_data)

        # Ignore all other position arguments except 'username' & 'password'
        username = json_data['username']
        password = json_data['password']

        return_value = login(username, password)

        return return_value

# helper classes
class Helper():
    def __init__(self):
        assert(os.path.isfile('./paths.csv'))
        self.dataset = pd.read_csv('./paths.csv')
        self.dataset_paths = self.dataset['path']

        api.add_resource(Image, '/image')
        api.add_resource(Login, '/login')
        
    def create_database(self):
        if os.path.isfile('./records.db'):
            reply = input("Do you want to delete currently existing database : ")
            if reply == 'y' or reply == 'Y':
                with app.app_context():
                    db.create_all()
                return
            else:
                return
        with app.app_context():
            db.create_all()
        
    def login(self, username, password):
        id = -1
        with app.app_context():
            user = User.query.filter_by(username=username, password=password).all()
            if len(user) == 1:
                id = user[0].id

        return id

    def insert_fake_users(self):
        admin = User(username='admin', password='adminPassword')
        guest = User(username='guest', password='guestPassword')
        test  = User(username='TestUsername', password='TestPassword')
        with app.app_context():
            db.session.add(admin)
            db.session.add(guest)
            db.session.add(test)
            db.session.commit()

    def delete_fake_users(self):
        with app.app_context():
            query_users = User.query.all()
            for user in query_users:
                db.session.delete(user)
            db.session.commit()

    def insert_fake_records(self):
        test1 = Record(item_id=1, item_category=1, user_id=1, rating=0)
        test2 = Record(item_id=1, item_category=1, user_id=2, rating=1)
        with app.app_context():
            db.session.add(test1)
            db.session.add(test2)
            db.session.commit()

    def delete_fake_records(self):
        with app.app_context():
            query_users = User.query.all()
            for user in query_users:
                db.session.delete(user)
            db.session.commit()

    def print_all_user_rows(self):
        with app.app_context():
            print('Rows : ', User.query.all())
        return 0

    def print_all_record_rows(self):
        with app.app_context():
            print('Rows : ', Record.query.all())
        return 0

    def print_all_tables(self):
        with app.app_context():
            print('Tables : ', db.engine.table_names())
        return 0

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk')
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Record(db.Model):
    id            = db.Column(db.Integer, nullable=False, primary_key=True, unique=True, autoincrement='ignore_fk')
    item_id       = db.Column(db.Integer, nullable=False)
    item_category = db.Column(db.Integer, nullable=False)
    user_id       = db.Column(db.Integer, nullable=False)
    rating        = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return_list = [self.id, self.item_id, self.item_category, self.user_id, self.rating]
        return str(return_list)

helper = Helper()
def login(username, password):
    return helper.login(username, password)

if __name__ == "__main__":
    # helper.create_database()
    # helper.insert_fake_users()
    # helper.insert_fake_records()
    # helper.print_all_record_rows()
    # helper.print_all_tables()
    # helper.print_all_user_rows()
    app.run(debug=True)