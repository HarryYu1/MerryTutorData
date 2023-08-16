from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SubmitField, SelectField, DateField, TextAreaField, SelectMultipleField, widgets
from wtforms.validators import InputRequired, Length
import flask_login #TODO implement tiered login system
from . import smtp
from . import session_summary_handler

sessionbp = Blueprint('session', __name__)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SessionForm(FlaskForm):
    tutor = StringField("Tutor Name (First Last):", validators=[InputRequired()])
    shadowingtutor = StringField("Shadowing Tutor (First Last):")
    date = DateField('Date Of Session:', validators=[InputRequired()])

    #tutee info
    tutee = StringField("Tutee Name (First Last):", validators=[InputRequired()])
    tuteegrade = SelectField('Grade Level:', choices = [(0, "K"), (1, 1), (2, 2), (3, 3), (4 , 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])
    parentemail = StringField("Parent Email:", validators=[InputRequired()])

    #location info
    location = SelectField('Location:', choices = [('nichols', 'Nichols Library'), ('alive', 'Alive Center'), ('95', '95th Street Library'), ('other', 'Other')]
                           , render_kw={'onchange': "changeTable()"})
    other_location = StringField('Please Specify:')

    #session info
    sessionlength = StringField('Session Length (In Minutes):', validators=[InputRequired()])
    subject = MultiCheckboxField('Subject:', choices = [('math', 'Math'), ('science', 'Science'), ('social_studies', 'Social Studies'), ('english', 'English')])
    other_subject = StringField('If Other Subject, Please Specify:')
    #the big entries
    summary = TextAreaField("What did you work on? What did the student do well? What did the student have trouble with?", 
                            validators=[InputRequired()], 
                            render_kw={"rows": 5, "cols": 60})
    suggestions = TextAreaField("What are some suggested steps until the next tutoring session? Any suggested homework?", 
                            validators=[InputRequired()], 
                            render_kw={"rows": 5, "cols": 60})
    submit = SubmitField("Submit")


@sessionbp.route('/session_summary', methods=['GET', 'POST'])
def render_session_form():
    form = SessionForm()
    if form.submit.data and form.validate_on_submit():
        print('submitted with button')
        session_summary_handler.handle_form(form)
        smtp.sendemail(subjects = form.subject.data, other_subjects = form.other_subject.data, tutorname = form.tutor.data, tuteename=form.tutee.data, summary = form.summary.data, suggestions = form.suggestions.data, email = form.parentemail.data)
        return redirect('/login')
    return render_template('session_form.html', form = form)