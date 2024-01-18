from sqlalchemy import URL
import sqlalchemy
import pandas as pd
import app

#########################################
#  Creates Accounts for Merry Tutor
#  Harry Yu 12/25/2023
#########################################


url_object = app.secretdata.url_object  #secret!

engine = sqlalchemy.create_engine(url_object)

#with engine.connect() as connection:

another = 'y' #sentry for loop


while (another == 'y'):
    name = input("Enter in name of Tutor (first last): ").lower()
    username = input("Enter in preferred username: ")
    password = input("Enter in password: ")

    name = [[name]] #make it suitable for constructor
    userData = pd.DataFrame(name, columns=['Name']) #initializer one row one column df
    userData["UserName"] = username
    userData["Password"] = password  #put in data into df

    print(userData)
 
    #result = connection.execute(sqlalchemy.text("select distinct Tutor from Attendance"))

    #df = pd.DataFrame(result.fetchall())
    #df.columns = result.keys()


    userData.to_sql(name = "Accounts", con = engine, if_exists='append', index = False) #index false is good

    another = input("Add another user (y, n)? ")

engine.dispose()

