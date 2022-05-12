# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# model the class after the friend table from our database
class Ninja:
    def __init__(self, data) :
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.courses = [] # n:m relationship

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dn_mn_flask_schema').query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninja with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojos_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojos_id)s, NOW() , NOW() );"
        return connectToMySQL('dn_mn_flask_schema').query_db(query, data)

    # Form Validation
    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        # age = int(ninja['age'])
        if len(ninja['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['age']) < 1:
            flash("Age must be not be empty.")
            is_valid = False
        elif int(ninja['age']) < 18:
            flash("Age must be over 18.")
            is_valid = False
        return is_valid