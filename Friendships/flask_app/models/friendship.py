# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_friend(cls, data):
        query = "INSERT INTO friendships(user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        return connectToMySQL('friendships_flask_schema').query_db(query, data)

    @classmethod
    def all_friendship(cls):
        query = "SELECT * FROM friendships;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('friendships_flask_schema').query_db(query)
        # Create an empty list to append our instances of authors
        friendships = []
        # Iterate over the db results and create instances of authors with cls.
        for friendship in results:
            friendships.append(cls(friendship))
        print(friendships)
        return friendships
    
    @classmethod
    def check_friendship_for_user(cls, data):
        query = "SELECT * FROM friendships WHERE user_id = %(user_id)s;"
        results = connectToMySQL('friendships_flask_schema').query_db(query, data)
        friendships = []
        # Iterate over the db results and create instances of authors with cls.
        for friendship in results:
            friendships.append(cls(friendship))
        print(friendships)
        return friendships