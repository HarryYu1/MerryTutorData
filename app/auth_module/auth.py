import flask
from flask import Blueprint, render_template
import flask_login
from flask import Flask, session, redirect, url_for, escape, request, g
from .. import secretdata


authbp = Blueprint('auth', __name__)


user1 =None
username  = None



class User:
   def __init__(self, id, username, password):
       self.id = id
       self.username = username
       self.password = password
  
   def __repr__(self):
       return f'<User: {self.username}>'
  


users = []
users.append(User(id = 1, username= 'Vinay', password = 'password'))
users.append(User(id = 2, username= 'Monkey', password = 'password'))






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
def login(): #chnaged to self 
   
   if flask.request.method == "GET":
       return render_template("login.html")
   username = flask.request.form["username"]
   password = flask.request.form["password"] 
   user1 = [x for x in users if x.username == username][0]
   if username in secretdata.users and flask.request.form['password'] == secretdata.users[username]['password']:
       user = User()
       user.id = username
       flask_login.login_user(user)
       return flask.redirect('/landing_page')
   
   elif user1 and user1.password == password:
       username = flask.request.form["username"]
       session['username_data'] = username
       return flask.redirect('/username/%s' % username)

   return flask.redirect('/login')





@authbp.route('/logout')
def logout():
   flask_login.logout_user()
   return flask.redirect('/login')


@login_manager.unauthorized_handler
def unauthorized_handler():
   return flask.redirect('login')
