import pandas
from datetime import datetime
import sqlalchemy
from sqlalchemy import URL
from .. import secretdata

'''
    name = StringField('Overseer Name', validators=[InputRequired()])
    date = DateField('Date Of Session:', validators = [InputRequired()])
    add_entry = SubmitField('Add Entry')
    delete_entry = SubmitField('Delete Entry')
    entries = FieldList(FormField(HourForm), min_entries=1)
    submit = SubmitField('Save')
'''

def handle_attendance(name, date, entries, location):
    print(name, date, entries)

    df = pandas.DataFrame(entries) 

    df.drop('csrf_token', axis = 1, inplace = True)
    #remove case sensitivity for board member
    name = name.lower()
    location = location.lower()
    #add the columns for name and date
    df['BoardMember'] = name
    df['DateOfHours'] = date
    df['Location'] = location

    #PREPROCESS FOR SQL
    #rename for sql
    df.rename(columns = {'tutorname':'Tutor', 'hours': 'Hours'}, inplace = True)
    
    #remove case sensitivity for tutors
    df['Tutor'] = df['Tutor'].str.lower()

    print(df) 

    #now we do the sql (skull emoji)
    engine = sqlalchemy.create_engine(secretdata.url_object)

    df.to_sql(name = "Attendance", con = engine, if_exists='append', index = False)

    engine.dispose()

def handle_comment(name, date, comment, location):

    data = [[name.lower(), date, comment, location.lower()]]
  
    # Create the pandas DataFrame
    df = pandas.DataFrame(data, columns=['BoardMember', 'DateOfHours', 'Comment', 'Location'])

    print(df)

    engine = sqlalchemy.create_engine(secretdata.url_object)

    df.to_sql(name = "Attendance_Comments", con = engine, if_exists='append', index = False)

    engine.dispose()