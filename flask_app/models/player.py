from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Player:
    def __init__(self,data):
        self.id = data["id"]
        self.position = data["position"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.team = data["team"]
        self.comments = data["comments"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None


    @classmethod
    def save(cls,data):
        query = "INSERT INTO players (position, first_name, last_name, team, comments, user_id) VALUES (%(position)s, %(first_name)s, %(last_name)s, %(team)s, %(comments)s, %(user_id)s);"
        result = connectToMySQL("fantasy_football_erd").query_db(query,data)
        return result

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM players LEFT JOIN users ON user_id = users.id "
        results = connectToMySQL("fantasy_football_erd").query_db(query)
        all_players = []
        for row_in_db in results:
            player_info = cls(row_in_db)
            user_data = {
                "id" : row_in_db["users.id"],
                "first_name" : row_in_db["users.first_name"],
                "last_name" : row_in_db["users.last_name"],
                "email" : row_in_db["email"],
                "password" : row_in_db["password"],
                "created_at" : row_in_db["created_at"],
                "updated_at" : row_in_db["updated_at"]
            }
            player_info.user = user.User(user_data)
            all_players.append(player_info)
            print("*****************")
            print(user_data)
        return all_players

    @classmethod
    def show_one(cls,id):
        query = " SELECT * FROM players WHERE id = %(id)s;"
        data = { "id" : id}
        results = connectToMySQL('fantasy_football_erd').query_db(query,data)
        return cls(results[0])

    @classmethod
    def edit_player(cls,data):
        query = """ UPDATE players
        SET position = %(position)s, first_name = %(first_name)s, last_name = %(last_name)s, team = %(team)s, comments = %(comments)s
        WHERE id = %(id)s; """
        return connectToMySQL('fantasy_football_erd').query_db('query,data')

    @classmethod
    def delete_player(cls,id):
        query = " DELETE FROM players WHERE id = %(id)s;"
        data = {"id" : id}
        return connectToMySQL("fantasy_football_erd").query_db(query,data)

    @staticmethod
    def validate_player(player):
        is_valid = True
        if len(player['position']) < 1:
            flash("Cannot leave position blank")
            is_valid = False
        if len(player['first_name']) < 1:
            flash("Cannot leave First Name blank")
            is_valid = False
        if len(player['last_name']) < 1:
            flash("Cannot leave Last Name blank")
            is_valid = False
        if len(player['team']) < 1:
            flash("Cannot leave Team blank")
            is_valid = False
        if len(player['comments']) < 5:
            flash("Cannot leave Comments blank")
            is_valid = False
        return is_valid



