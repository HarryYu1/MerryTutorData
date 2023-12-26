import flask
from flask import Blueprint, render_template, session, redirect
import flask_login
from .. import secretdata
import sqlalchemy

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
    print(request)
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
    if username in secretdata.users and flask.request.form['password'] == secretdata.users[username]['password']:  #admin
        user = User()
        user.id = username
        flask_login.login_user(user)
        return flask.redirect('/landing_page') 
    else:    #tutor login
       name = validateTutorLogin(username, flask.request.form['password'])
       if len(name) != 0: #if exists
        session['username_data'] = str(name[0][0]) #unpack the name, also its a key now (see stats.py for jank details)
        return flask.redirect('/tutor/%s' % username)
       print('invalid login.')
       return flask.redirect('/login')

    

 
def validateTutorLogin(user, password):   #check if username and associated password exists
    engine = sqlalchemy.create_engine(secretdata.url_object)

    with engine.connect() as connection:
        sql = sqlalchemy.text("select Name from Accounts where Username = \'" + user + "\' and Password = \'" + password + "\'")

        result = connection.execute(sql)

        connection.close()

        engine.dispose()
        
        return result.fetchall()
    





@authbp.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect('/login')

@login_manager.unauthorized_handler
def unauthorized_handler():
    return flask.redirect('login')