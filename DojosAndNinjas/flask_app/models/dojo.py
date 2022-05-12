# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from pprint import pprint
from flask import flash
# dojo model
class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = [] # n:1 relationship

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dn_mn_flask_schema').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # create new dojo method
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dn_mn_flask_schema').query_db(query, data)

    # find one dojo by id
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dn_mn_flask_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # find one dojo with all ninjas in it
    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dn_mn_flask_schema').query_db( query , data )
        # results will be a list of ninja objects with the dojo attached to each row. 
        if len(results) < 1:
            return False
        else:
            dojo = cls( results[0] )
            pprint(dojo)
        
            for row_from_db in results:
                # print(row_from_db)
                # Now we parse the ninja data to make instances of ninjas and add them into our list.
                ninja_data = {
                    "id" : row_from_db["ninjas.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "age" : row_from_db["age"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"]
                }
                dojo.ninjas.append( ninja.Ninja( ninja_data ) )
            return dojo   
        
    # Form Validation
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid