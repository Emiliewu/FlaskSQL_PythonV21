# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship

class User:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('friendships_flask_schema').query_db(query)
        # Create an empty list to append our instances of authors
        users = []
        # Iterate over the db results and create instances of authors with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO users ( first_name, last_name, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, NOW(),NOW());"
        return connectToMySQL('friendships_flask_schema').query_db(query, data)

    @classmethod
    def get_all_users_with_friends(cls):
        query = "SELECT users.first_name, users.last_name, friends.first_name AS friend_first_name, friends.last_name AS friend_last_name FROM users LEFT JOIN friendships ON user_id = users.id LEFT JOIN users AS friends ON friend_id = friends.id;"
        results = connectToMySQL('friendships_flask_schema').query_db(query)
        print(results)
        friends = []
        for friend in results:
            friends.append(friend)
        return friends