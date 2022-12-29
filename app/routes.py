from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Scott"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("index.html", title="Scott", user=user, posts=posts)


@app.route("/test")
def test():
    return "Hi there"
