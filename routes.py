import random
import pandas as pd

from pprint import pprint
from flask import Flask, request
from flask_restful import Resource

dataset = pd.read_csv('./paths.csv')
dataset_paths = dataset['path']

class Image(Resource):
    def get(self):
        return random.choice(dataset['path'])


class Login(Resource):
    def get(self):
        return "Do not try to get Login"

    def post(self):
        json_data = request.get_json(force=True)
        pprint(json_data)
        # Ignore all other position arguments except 'username' & 'password'
        username = json_data['username']
        password = json_data['password']

        return 0



if __name__ == "__main__":
    print(random.choice(dataset['path']))