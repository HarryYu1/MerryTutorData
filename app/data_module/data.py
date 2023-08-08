from flask import Flask, render_template_string
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import FormField, StringField, SubmitField, SelectField, DateField, BooleanField
from wtforms.validators import InputRequired
import flask_login
from . import handle_data

databp = Blueprint('data', __name__)

class QueryForm(FlaskForm):
    table = SelectField('Table To Query:', choices = [('attendance', 'Attendance'), ('attendance_comments', 'Attendance Comments'), ('sessions', 'Session Summaries')], 
                        validators=[InputRequired()], default = 'attendance', render_kw={'onchange': "changeTable()"})
    
    attendance_function = SelectField('Function:', choices = [('graph','Graph'), ('sum','Sum'), ('query', 'General Query')]) #value label pairs
    attendance_comments_function = SelectField('Function:', choices = [('bayes', 'Naive Bayes'), ('query', 'General Query')])
    sessions_function = SelectField('Function:', choices = [('location', 'Location Distribution'), ('graph', 'Graph'), ('query', 'General Query')])
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

    #TODO add a bunch of validation here
    if request.method == 'POST': 
        handle_data.handle_form(table = form.table.data, attendance_function=form.attendance_function.data,
                                attendance_comments_function=form.attendance_comments_function.data, 
                                sessions_function=form.sessions_function.data, 
                                toggle_range=form.toggle_range.data, singledate=form.singledate.data, 
                                startdate=form.start_date.data, enddate=form.end_date.data,
                                tutor=form.tutor.data)
        return redirect('/landing_page')

    return render_template("dataform.html" ,form=form)