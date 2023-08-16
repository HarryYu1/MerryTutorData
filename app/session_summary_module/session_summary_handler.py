import sqlalchemy
from .. import secretdata
import pandas

def handle_form(form):
    #initialize 
    data = [[form.tutor.data]]
    df = pandas.DataFrame(data, columns=['Tutor'])

    #put all the values in
    #df['Tutor'] = form.tutor.data
    df['ShadowingTutor'] = form.shadowingtutor.data
    df['Date'] = form.date.data
    df['Tutee'] = form.tutee.data
    df['TuteeGrade'] = form.tuteegrade.data
    df['TuteeGrade'] = pandas.to_numeric(df['TuteeGrade']) #change to numeric so sum and average works
    df['ParentEmail'] = form.parentemail.data
    #validate location
    if form.location.data == 'other':
        df['Location'] = form.other_location.data
    else:
        df['Location'] = form.location.data
    df['SessionLength'] = form.sessionlength.data
    df['SessionLength'] = pandas.to_numeric(df['SessionLength'])
    list_of_subjects = form.subject.data
    if form.other_subject.data:
        list_of_subjects.append(form.other_subject.data)
    df['Subject'] = ' '.join(list_of_subjects)  #join to string and add
    df['Summary'] = form.summary.data
    df['Suggestions'] = form.suggestions.data

    print(df)

    #hopefully this works type stuff
    engine = sqlalchemy.create_engine(secretdata.url_object)

    df.to_sql(name = "Session_Summaries", con = engine, if_exists='append', index = False)

    engine.dispose()