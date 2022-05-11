# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self, data):
        self.books_id = data['books_id']
        self.authors_id = data['authors_id']

    @classmethod
    def create_favorite(cls, data):
        query = "INSERT INTO favorites(books_id, authors_id) VALUES (%(books_id)s, %(authors_id)s);"
        return connectToMySQL('books_flask_schema').query_db(query, data)