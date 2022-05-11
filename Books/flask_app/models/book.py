# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    def __init__( self, data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_flask_schema').query_db(query)
        # Create an empty list to append our instances of book
        books = []
        # Iterate over the db results and create instances of books with cls.
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s,NOW(), NOW());"
        return connectToMySQL('books_flask_schema').query_db(query, data)

    # This method will retrieve the specific book along with all the authors associated with it.
    @classmethod
    def get_book_with_authors( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.books_id = books.id LEFT JOIN authors ON favorites.authors_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_flask_schema').query_db( query , data )
        # results will be a list of authors objects with the book attached to each row. 
        if results:
            books = cls( results[0] )
        else:
            return "not found"
        for row_from_db in results:
            # Now we parse the author data to make instances of book and add them into our list.
            author_data = {
                "id" : row_from_db["authors.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            books.authors.append( author.Author( author_data ) )
        return books

    # #find all books not favorite by one author
    @classmethod
    def find_books_not_favorite_byoneauthor(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT books_id FROM favorites WHERE authors_id = %(id)s);"
        results = connectToMySQL('books_flask_schema').query_db( query , data )
        books = []
        for book in results:
            books.append(cls(book))
        return books