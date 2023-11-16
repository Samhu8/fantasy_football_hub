from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models import user
from flask_app.models import comment


@app.route('/comments')
def comments():
    data = {
        "id" : session["user_id"]
    }
    user_info = user.User.get_by_id(data)
    comments = comment.Comments.show_all()
    return render_template('comments.html', user = user_info, all_comments = comments )

@app.route('/comments', methods=['POST'])
def save():
    data = {
        "comments" : request.form["comments"],
        "user_id" : session["user_id"]
    }
    comment.Comments.save(data)
    comments = comment.Comments.show_all()
    return redirect("/comments")