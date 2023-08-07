from flask import Flask, render_template_string
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import FormField, StringField, SubmitField, SelectField, DateField, BooleanField
from wtforms.validators import InputRequired
import flask_login

databp = Blueprint('data', __name__)

class QueryForm(FlaskForm):
    function = SelectField('Function', choices = [('trend','Trend'), ('sum','Sum')], validators = [InputRequired()]) #value label pairs
    #super annoying toggle checkbox
    toggle_range = BooleanField('Query Range:', render_kw={'onchange': "toggleRange()"})
    singledate = DateField('Date To Query:')
    start_date = DateField('Start Date:')
    end_date = DateField('End Date:')
    tutor = StringField('Specific Tutor (Optional):')
    submit = SubmitField('Submit')

@databp.route('/data', methods = ['GET', 'POST'])
@flask_login.login_required
def render_data_form():
    form = QueryForm()

    if form.validate_on_submit():
        print(form.function.data)
        print(form.end_date.data)

        return redirect('/landing_page')

    return render_template("dataform.html" ,form=form)