import flask
from flask import Flask, render_template_string, redirect
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from .. import secretdata
import sqlalchemy
import pandas as pd



statsbp = Blueprint('stats', __name__)

@statsbp.route('/tutor/<string:user_name>/', methods=['GET', 'POST'])
def displaydata(user_name):  #username is string username prefiltered in auth
    #user = flask.request.form["username"]
    if session.get('username_data'):
        username = session.pop('username_data') #JANK ASS SYSTEM - treat session data as a key, take it away unless they do specific submission thing
        attendance = grab_attendance_for(username)
        sessions = grab_sessions_for(username)
        print(username)
        return render_template('stats.html',  attendanceTable=[attendance.to_html(classes='data', header="true")], 
                               sessionsTable = [sessions.to_html(classes='data', header="true")])
    else:
        print('no tutor login')
        return redirect('/login')

#grab attendance df from db
def grab_attendance_for(username):
    engine = sqlalchemy.create_engine(secretdata.url_object)

    with engine.connect() as connection:
        sql = sqlalchemy.text("select * from Attendance where Tutor = \'" + username + "\' order by DateOfHours desc")

        result = connection.execute(sql)

        connection.close()

        engine.dispose()
        
    df = pd.DataFrame(result.fetchall())
    return df

#grab session df from db
def grab_sessions_for(username):
    engine = sqlalchemy.create_engine(secretdata.url_object)

    with engine.connect() as connection:
        sql = sqlalchemy.text("select * from Session_Summaries where Tutor = \'" + username + "\' order by Date desc")

        result = connection.execute(sql)

        connection.close()

        engine.dispose()
        
    df = pd.DataFrame(result.fetchall())
    return df

