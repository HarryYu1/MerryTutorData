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

    from .landing_module import landing
    app.register_blueprint(landing.landingbp)

    from .attendance_module import attendance
    app.register_blueprint(attendance.attendancebp)

    from .data_module import data
    app.register_blueprint(data.databp)

    from .session_summary_module import session_summary
    app.register_blueprint(session_summary.sessionbp)

    #hooray error handler
    @app.errorhandler(500)
    def internal_error(error):

        return str(error) #replace with a good page later

    return app

