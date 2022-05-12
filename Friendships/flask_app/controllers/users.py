
from flask_app import app
from flask import render_template,redirect,request,session,get_flashed_messages
from flask_app.models.user import User

from flask_app.models.friendship import Friendship

@app.route("/")
@app.route("/friendships")
def index():
    # call the get all classmethod to get all friends
    friendships = User.get_all_users_with_friends()
    users = User.get_all()
    return render_template("index.html", friendships = friendships, users = users)

@app.route("/users/new", methods=['POST'])
def createuser():
    data = {
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"],
    }
    User.save(data)
    return redirect("/friendships")

@app.route("/friendships/new", methods=['POST'])
def createfriendship():
    user_id = int(request.form["user"])
    friend_id = int(request.form["friend"])
    data = {
        "user_id": request.form["user"],
        "friend_id": request.form["friend"]
    }

    friendships = Friendship.all_friendship()
    print(friendships)
    for friend in friendships:
        if friend.user_id  == user_id and friend.friend_id == friend_id:
            return redirect("/friendships")
        elif friend.friend_id == user_id and friend.user_id == friend_id:
            return redirect("/friendships")
        elif user_id == friend_id:
            return redirect("/friendships")
    
    Friendship.add_friend(data)
    return redirect("/friendships")