# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = [] # n:m relationship
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_flask_schema').query_db(query)
        # Create an empty list to append our instances of authors
        authors = []
        # Iterate over the db results and create instances of authors with cls.
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES (%(name)s, NOW(),NOW());"
        return connectToMySQL('books_flask_schema').query_db(query, data)

    # This method will retrieve the specific author along with all the books associated with it.
    @classmethod
    def get_author_with_books( cls , data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.authors_id = authors.id LEFT JOIN books ON favorites.books_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_flask_schema').query_db( query , data )
        # results will be a list of books objects with the author attached to each row. 
        if results:
            author = cls( results[0] )
        else:
            return "not found"
        for row_from_db in results:
            # Now we parse the author data to make instances of books and add them into our list.
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.books.append( book.Book( book_data ) )
        return author

    # https://login.codingdojo.com/m/172/7218/52112 sql references
    # https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial

    @classmethod
    def find_authors_not_favorite_onebook(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT authors_id FROM favorites WHERE books_id = %(id)s);"
        results = connectToMySQL('books_flask_schema').query_db( query , data )
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors