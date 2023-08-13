from flask import Flask, render_template_string
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length
import flask_login
from . import attendance_form_handler

attendancebp = Blueprint('attendance', __name__)

#single attendance entry
class HourForm(FlaskForm):
    tutorname = StringField('Name')
    hours = SelectField('Hours', choices = [(0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2)])  #value label pairs

class AttendanceForm(FlaskForm):
    name = StringField('Overseer Name', validators=[InputRequired()])
    date = DateField('Date Of Session:', validators=[InputRequired()])
    location = SelectField('Location:', choices = [('nichols', 'Nichols Library'), ('alive', 'Alive Center'), ('95', '95th Street Library'), ('other', 'Other')]
                           , render_kw={'onchange': "changeTable()"})
    other_location = StringField('Please Specify:')
    add_entry = SubmitField('Add Entry')
    delete_entry = SubmitField('Delete Entry')
    entries = FieldList(FormField(HourForm), min_entries=1)
    optional_comment = TextAreaField('Additional Comments:', render_kw={"rows": 5, "cols": 20}, validators=[Length(max=200)])
    redirect_landing = SubmitField('Back')
    submit = SubmitField('Submit')



@attendancebp.route('/attendance', methods=['GET', 'POST'])
@flask_login.login_required
def attendance():
    form = AttendanceForm()

    if form.add_entry.data:  #if submitted via add entry
      form.entries.append_entry(None)
    elif form.delete_entry.data:
        form.entries.pop_entry()

    elif form.redirect_landing.data:
        return redirect("/landing_page") #janky, but redirects back first before any actual sql stuff happens

    elif form.validate_on_submit():
        #for entry in form.entries.data:
        #    print(entry)
        if form.location.data == "other":
            attendance_form_handler.handle_attendance(name = form.name.data, date = form.date.data, entries = form.entries.data, location= form.other_location.data)
        else:
            attendance_form_handler.handle_attendance(name = form.name.data, date = form.date.data, entries = form.entries.data, location= form.location.data)  
            #add error handling with return value
        #    redirect to error page
        if form.optional_comment.data:
            if form.location.data == "other":
                attendance_form_handler.handle_comment(name = form.name.data, date = form.date.data, comment = form.optional_comment.data, location = form.other_location.data)
            else:
                attendance_form_handler.handle_comment(name = form.name.data, date = form.date.data, comment = form.optional_comment.data, location = form.location.data)

        return redirect('/landing_page')

        #now redirect to landing or something
    return render_template("attendance.html" ,form=form)