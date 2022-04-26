from flask import Flask, render_template, redirect, request, url_for, flash, send_from_directory, session
import os

app = Flask(__name__)
app.secret_key = "XMLDJfijEr"


@app.route("/")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080
    )
