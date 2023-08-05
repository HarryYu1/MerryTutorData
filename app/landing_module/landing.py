from flask import Blueprint, render_template
import flask
import flask_login



landingbp = Blueprint('landing', __name__)
@flask_login.login_required
@landingbp.route('/landing_page', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing.html')