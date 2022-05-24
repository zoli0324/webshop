from flask import Flask, render_template, redirect, request, url_for, flash, send_from_directory, session
from werkzeug.utils import secure_filename
import os
import util
import password_handler

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = "XMLDJfijEr"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def main_page():
    return render_template("index.html")


# # # USER SETTING # # #


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    if util.check_username(username) is False:
        if password_handler.verify_password(request.form["password"], util.user_login(username)):
            session.permanent = True
            session["username"] = request.form["username"]
            session["is_admin"] = util.is_admin(username)
    return redirect("/")


@app.route("/registration", methods=["POST"])
def registration():
    username = request.form["new-username"]
    fist_name = request.form["firstname"]
    last_name = request.form["lastname"]
    password = request.form["new-password"]
    repeat_pw = request.form["repeat-password"]
    check_username = util.check_username
    if password == repeat_pw and check_username(username) is True:
        util.user_registration(username, fist_name, last_name, password_handler.hash_password(password))
        session.permanent = True
        session["username"] = username
    return redirect("/")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect("/")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template("profile.html")
    else:
        old_password = password_handler.hash_password(request.form["old-password"])
        if password_handler.verify_password(request.form["old-password"], old_password):
            if request.form["password"] == request.form["password-repeat"]:
                util.change_password(session["username"], password_handler.hash_password(request.form["password"]))
    return redirect("/")


@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("management.html")
    else:
        category = request.form["category"]
        product_name = request.form["product-name"]
        description = request.form["description"]
        price = request.form["price"]
        in_stock = request.form["in-stock"]
        util.add_product(category, product_name, description, price, in_stock)
    return redirect("/")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080
    )
