
from flask_app import app
from flask import render_template,redirect,request,session,get_flashed_messages
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite

@app.route("/")
@app.route("/authors")
def index():
    # call the get all classmethod to get authors
    authors = Author.get_all()
    print(authors)
    return render_template("index.html", authors = authors)

# create new author
@app.route("/authors/new", methods=['POST'])
def createauthor():
    data = {
        'name': request.form['name']
    }
    Author.save(data)
    return redirect("/authors")

@app.route("/books")
def newbook():
    # create new book
    books = Book.get_all()
    return render_template("newbook.html", books = books)

@app.route("/books/new", methods=['POST'])
def createbook():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.save(data)
    return redirect("/books")

@app.route("/books/<int:id>")
def booksdetail(id):
    # display books detail
    data = {
        "id": id
    }
    book = Book.get_book_with_authors(data)
    otherauthors = Author.find_authors_not_favorite_onebook(data)
    return render_template("bookdetail.html", book = book, authors = otherauthors)

@app.route("/authors/<int:id>")
def authorsdetail(id):
    # display authors detail
    data = {
        "id": id
    }
    author = Author.get_author_with_books(data)
    otherbooks = Book.find_books_not_favorite_byoneauthor(data)
    
    return render_template("authordetail.html", author = author, books = otherbooks)

# create favorite relationship
@app.route("/favorite/new", methods=['POST'])
def newfavorite():
    
    data = {
        'books_id': request.form['book'],
        'authors_id': request.form['author']
    }
    Favorite.create_favorite(data)
    return redirect('/')
