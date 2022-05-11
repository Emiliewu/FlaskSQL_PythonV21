from flask_app.config.mysqlconnection import connectToMySQL

class Registration:
    def __init__(self, data):
        self.ninjas_id = data['ninjas_id']
        self.courses_id = data['courses_id']

    @classmethod
    def register_ninja_to_course(cls, data):
        query = "INSERT INTO registrations(ninjas_id, courses_id) VALUES (%(ninja_id)s, %(course_id)s);"
        return connectToMySQL('dn_mn_flask_schema').query_db(query, data)