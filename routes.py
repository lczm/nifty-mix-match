import csv
import random
import pandas as pd

from flask_restful import Resource

dataset = pd.read_csv('./paths.csv')
dataset_paths = dataset['path']

class Image(Resource):
    def get(self):
        return random.choice(dataset['path'])


if __name__ == "__main__":
    print(random.choice(dataset['path']))