import flask
from flask import Blueprint, render_template
import flask_login
from .. import secretdata

authbp = Blueprint('auth', __name__)

#initialize login manager
login_manager = flask_login.LoginManager()

@authbp.record_once
def on_load(state):
    login_manager.init_app(state.app)

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(name):
    if name not in secretdata.users:
        return

    user = User()
    user.id = name
    return user


@login_manager.request_loader
def request_loader(request):
    name = request.form.get('Username')
    if name not in secretdata.users:
        return

    user = User()
    user.id = name
    return user


@authbp.route("/login", methods = ["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return render_template("login.html")
    
    username = flask.request.form["username"]
    if username in secretdata.admins and flask.request.form['password'] == secretdata.admins[username]['password']:  #admin login
        user = User()
        user.id = username
        flask_login.login_user(user)  #login admin user TODO
        return flask.redirect('/landing_page')   
    elif username in secretdata.users and flask.request.form['password'] == secretdata.users[username]['password']:
        return flask.redirect('/session_summary')  #login normal user TODO
    
    return flask.redirect('/login')


@authbp.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect('/login')

@login_manager.unauthorized_handler
def unauthorized_handler():
    return flask.redirect('login')
