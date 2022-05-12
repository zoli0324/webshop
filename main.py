from flask import Flask, render_template, redirect, request, url_for, flash, send_from_directory, session
import os
import util
import password_handler

app = Flask(__name__)
app.secret_key = "XMLDJfijEr"


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(util.check_username(username))
    if(util.check_username(username) is False):
        hashed_password = util.user_login(username)
        if(password_handler.verify_password(password, hashed_password)):
            session.permanent = True
            session["username"] = request.form["username"]
    return redirect("/")


@app.route("/registration", methods=["POST"])
def registration():
    username = request.form["new-username"]
    fist_name = request.form["firstname"]
    last_name = request.form["lastname"]
    password = request.form["new-password"]
    repeat_pw = request.form["repeat-password"]
    check_username = util.check_username(username)
    if(password == repeat_pw and check_username is True):
        util.user_registration(username, fist_name, last_name, password_handler.hash_password(password))
        session.permanent = True
        session["username"] = username
    return redirect("/")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None)
    return redirect("/")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080
    )
