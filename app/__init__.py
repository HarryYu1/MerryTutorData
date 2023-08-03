from flask import Flask
import flask
from . import secretdata
import flask_login

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretdata.SECRET_KEY
    app.secret_key = secretdata.SECRET_KEY

    @app.route("/", methods = ["GET", "POST"])
    def redirect_login():
        return flask.redirect("/login")

    #blueprints here
    from .auth_module import auth
    app.register_blueprint(auth.authbp)

    from .attendance_module import attendance
    app.register_blueprint(attendance.attendancebp)



    return app