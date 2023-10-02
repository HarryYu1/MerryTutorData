import flask
from flask import Flask, render_template_string
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for




statsbp = Blueprint('stats', __name__)

@statsbp.route('/username/<string:user_name>/', methods=['GET', 'POST'])
def username(user_name):
    #user = flask.request.form["username"]
    username = session.get('username_data')
    result = username
    return render_template("stats.html", result=result)
def stats():
    return  "done"

