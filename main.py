from flask import Flask, render_template, redirect, request, url_for, flash, send_from_directory, session
import os

app = Flask(__name__)
app.secret_key = "XMLDJfijEr"


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return redirect("/")


@app.route("/registration", methods=["POST"])
def registration():
    username = request.form["new-username"]
    password = request.form["new-password"]
    repeat_pw = request.form["repeat-password"]
    print(username + password + repeat_pw)
    return redirect("/")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080
    )
