from flask_app import app
from flask import redirect,request,render_template,session,flash
from flask_app.models import user
from flask_app.models import player


# ************ ADDING A NEW PLAYER ************

@app.route('/new_player')
def new_player():
    data = {
        "id" : session["user_id"]
    }
    logged_in_user = user.User.get_by_id(data)
    return render_template('new_player.html', person = logged_in_user)

@app.route('/new_player', methods=['POST'])
def create_player():
    if not player.Player.validate_player(request.form):
        return redirect('/new_player')
    data = {
        "position" : request.form["position"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "team" : request.form["team"],
        "comments" : request.form["comments"],
        "user_id" : session["user_id"]
    }
    player.Player.save(data)
    return redirect ('/login')

# ************ EDIT PLAYER ************

@app.route('/edit/<int:id>')
def edit_player(id):
    player_info = player.Player.show_one(id)
    return render_template('edit.html', player = player_info)

# ************ DELETE PLAYER ************

@app.route('/delete/<int:id>')
def delete_player(id):
    player.Player.delete_player(id)
    return redirect('/login')


@app.route('/games')
def test():
    return render_template('games.html')