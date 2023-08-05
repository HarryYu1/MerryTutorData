import pandas
from datetime import datetime

'''
    name = StringField('Overseer Name', validators=[InputRequired()])
    date = DateField('Date Of Session:', validators = [InputRequired()])
    add_entry = SubmitField('Add Entry')
    delete_entry = SubmitField('Delete Entry')
    entries = FieldList(FormField(HourForm), min_entries=1)
    submit = SubmitField('Save')
'''

def handle_attendance(name, date, entries):
    print(name, date, entries)

    df = pandas.DataFrame(entries) 

    df.drop('csrf_token', axis = 1, inplace = True)
    df['BoardMember'] = name
    df['DateOfHours'] = date

    #rename for sql
    df.rename(columns = {'tutorname':'Tutor', 'hours': 'Hours'}, inplace = True)

    print(df) 

