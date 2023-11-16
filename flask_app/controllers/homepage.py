from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def main():
    if session.get("user_id"):
        return redirect("/login")
    return render_template('index.html')

