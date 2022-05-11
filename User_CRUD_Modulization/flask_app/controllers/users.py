from flask_app import app
from flask import render_template,redirect,request,session,get_flashed_messages
from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route("/new")
def userform():
    return render_template("create.html")

@app.route("/create", methods=['POST'])
def newuser():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect("/")

@app.route("/detail/<int:id>")
def show(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    print(user)
    return render_template("show.html", user = user)

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    print(user)
    return render_template("edit.html", user = user)

@app.route("/update", methods=['POST'])
def updateuser():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.update(data)
    # Don't forget to redirect after saving to the database.
    return redirect("/")
    
@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/")