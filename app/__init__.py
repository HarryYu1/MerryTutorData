from flask import Flask


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "mysupersecretkey"

    #blueprints here

    from .attendance_module import attendance
    app.register_blueprint(attendance.attendancebp)

    from .auth_module import auth
    app.register_blueprint(auth.authbp)

    return app