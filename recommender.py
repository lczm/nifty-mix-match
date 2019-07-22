import numpy as np
import pandas as pd

from tqdm import tqdm
from pprint import pprint
from keras.models import Model, load_model
from keras.layers import Input, Embedding, Flatten, Dot, Dense

from sklearn.model_selection import train_test_split

class Recommender():
    def __init__(self):
        self.dataset = pd.read_csv('./paths.csv')
        self.unique_users    = len(self.dataset.user_id.unique())
        self.unique_clothing = len(self.dataset.clothing_id.unique())
        self.model = None

    def build_model(self):
        user_input = Input(shape=[1], name="User-Input")
        user_embedding = Embedding(self.unique_users+1, 5, name="User-Embedding")(user_input)
        user_vec = Flatten(name="Flatten-Users")(user_embedding)

        clothing_input = Input(shape=[1], name="Book-Input")
        clothing_embedding = Embedding(self.unique_clothing+1, 5, name="Clothes-Embedding")(clothing_input)
        clothing_vec = Flatten(name="Flatten-Clothes")(clothing_embedding)

        prod = Dot(name="Dot-Product", axes=1)([user_vec, clothing_vec])
        model = Model([user_input, clothing_input], prod)
        model.compile('adam', 'mean_squared_error')
        self.model = model
        return 0

    def train_model(self):
        return 0

    def save_model(self, name="model.h5"):
        self.model.save(name)
        return 0

    def load_model(self, name="model.h5"):
        self.model = load_model(name)
        return 0

    def predict(self):
        # users = np.array([1 for i in range(len()])
        # book_data = np.array(list(set(dataset.book_id)))
        # user = np.array([2 for i in range(len(book_data))])

        # predictions = model.predict([user, book_data])
        # predictions = np.array([a[0] for a in predictions])

        # recommended_book_ids = (-predictions).argsort()[:5]
        # print(recommended_book_ids)
        # print(predictions[recommended_book_ids])
        # final_recommendations = books[books['id'].isin(recommended_book_ids)]
        return 0


class BookRecommender():
    def __init__(self):
        self.dataset = pd.read_csv('./recommendertest/ratings.csv')
        self.unique_users = len(self.dataset.user_id.unique())
        self.unique_books = len(self.dataset.book_id.unique())
        self.model = None
        self.train, test = train_test_split(self.dataset, test_size=0.2, random_state=42)

    def build_model(self):
        user_input = Input(shape=[1], name="User-Input")
        user_embedding = Embedding(self.unique_users+1, 5, name="User-Embedding")(user_input)
        user_vec = Flatten(name="Flatten-Users")(user_embedding)

        book_input = Input(shape=[1], name="Book-Input")
        book_embedding = Embedding(self.unique_books+1, 5, name="Book-Embedding")(book_input)
        book_vec = Flatten(name="Flatten-Book")(book_embedding)

        prod = Dot(name="Dot-Product", axes=1)([user_vec, book_vec])
        model = Model([user_input, book_input], prod)
        model.compile('adam', 'mean_squared_error')
        self.model = model
        return 0

    def train_model(self):
        history = self.model.fit([self.train.user_id, self.train.book_id], self.train.rating, epochs=3, verbose=1)
        return 0

    def save_model(self, name="model.h5"):
        self.model.save(name)
        return 0

    def load_model(self, name="model.h5"):
        self.model = load_model(name)
        return 0

    def predict(self):
        book_data = np.array(list(set(self.dataset.book_id)))
        user = np.array([2 for i in range(len(book_data))])

        predictions = self.model.predict([user, book_data])
        predictions = np.array([a[0] for a in predictions])

        recommended_book_ids = (-predictions).argsort()[:5]
        print(recommended_book_ids)

        books = pd.read_csv('./recommendertest/books.csv')

        final_recommendations = books[books['id'].isin(recommended_book_ids)]
        print(final_recommendations)
        return 0




if __name__ == "__main__":
    recommender = BookRecommender()
    # recommender.build_model()
    # recommender.train_model()
    # recommender.save_model()
    recommender.load_model()
    recommender.predict()
