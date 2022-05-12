from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask import flash

class Course:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = [] # n:m relationship
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM courses;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dn_mn_flask_schema').query_db(query)
        # Create an empty list to append our instances of courses
        courses = []
        # Iterate over the db results and create instances of course with cls.
        for course in results:
            courses.append(cls(course))
        return courses

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO courses ( name, created_at, updated_at ) VALUES (%(name)s, NOW(),NOW());"
        return connectToMySQL('dn_mn_flask_schema').query_db(query, data)

    # This method will retrieve the specific course along with all the ninjas registered with it.
    @classmethod
    def get_course_with_ninjas( cls , data ):
        query = "SELECT * FROM courses LEFT JOIN registrations ON registrations.courses_id = courses.id LEFT JOIN ninjas ON registrations.ninjas_id = ninjas.id WHERE courses.id = %(id)s;"
        results = connectToMySQL('dn_mn_flask_schema').query_db( query , data )
        # results will be a list of ninjas objects with the course attached to each row. 
        if results:
            course = cls( results[0] )
        else:
            return "not found"
        for row_from_db in results:
            # Now we parse the ninja data to make instances of course and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "name" : row_from_db["name"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            course.ninjas.append( ninja.Ninja( ninja_data ) )
        return course

       # Form Validation
    @staticmethod
    def validate_course(course):
        is_valid = True # we assume this is true
        if len(course['name']) < 3:
            flash("Course Name must be at least 3 characters.")
            is_valid = False
        return is_valid

