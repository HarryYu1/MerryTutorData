import flask
from flask import Blueprint, render_template

authbp = Blueprint('auth', __name__)

@authbp.route("/", methods = ["GET", "POST"])
def login():
    return render_template("login.html")