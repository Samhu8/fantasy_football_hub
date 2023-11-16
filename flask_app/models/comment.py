from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import user
from flask import flash

class Comments:
    def __init__(self, data):
        self.id = data["id"]
        self.comments = data["comments"]
        self.created_at = data["created_at"]
        self.updated_at = data["created_at"]
        self.user_id = data["user_id"]
        self.user = None


    @classmethod
    def save(cls,data):
        query = " INSERT INTO comments (comments, user_id) VALUES (%(comments)s,%(user_id)s);"
        result = MySQLConnection('fantasy_football_erd').query_db(query,data)
        return result

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM comments LEFT JOIN users ON user_id = users.id;"
        result = MySQLConnection('fantasy_football_erd').query_db(query)
        all_comments = []
        for row_in_db in result:
            user_info = cls(row_in_db)
            user_data = {
                "id" : row_in_db["users.id"],
                "first_name" : row_in_db["first_name"],
                "last_name" : row_in_db["last_name"],
                "email" : row_in_db["email"],
                "password" : row_in_db["password"],
                "created_at" : row_in_db["users.created_at"],
                "updated_at" : row_in_db["updated_at"]
            }
            user_info.user = user.User(user_data)
            all_comments.append(user_info)
        return all_comments

