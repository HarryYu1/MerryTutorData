

#big ol catch all
def handle_form(table, attendance_function, attendance_comments_function, sessions_function, toggle_range, singledate, startdate, enddate, tutor):
    '''
    Bunch of pseudo code
    
    
    if table = attendance:
        if toggle_range: #this is if togglerange is true, meaning there's two dates not single
            if block for each function type
            ex:
            if attendance_function = sum:
                sum(startdate, enddate, tutor)
        else:
            do the same but for a single date version of each function
    write elifs for the different tables
    
    '''
    print(table, attendance_function, attendance_comments_function, sessions_function, toggle_range, singledate, startdate, enddate, tutor)