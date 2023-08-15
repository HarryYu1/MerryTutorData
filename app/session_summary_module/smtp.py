from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib


def sendemail(tutorname, tuteename, summary, suggestions, email):
    smtp = smtplib.SMTP('smtp.gmail.com', 587) #connect to the gmail smtp server
    smtp.ehlo()  #initiate the connection with extended hello
    smtp.starttls() #begin encryption for message transfer
    #smtp.login('hyu.harryyu@gmail.com', 'ijzfcjlzactlcpcc') #app password
    smtp.login('naperville.themerrytutor@gmail.com', 'ddnaoeznqlowyetx')

    msg = MIMEMultipart() #empty multipart function
    msg['Subject'] = 'Tutoring Session Summary for %s with The Merry Tutor' % tuteename.title()

    msgintro = '''
Dear guardians of %s,

Thank you for tutoring with The Merry Tutor! This email is an automatically generated session summary for %s. If you would like to tutor with us again, please visit our website for our Zoom link on the next available day.

We would appreciate your feedback on this brief Session Feedback Survey so we can make your child's tutoring experience even better!  If you have any further comments or concerns, feel free to shoot us an email and we will get back as soon as possible.

''' % (tuteename.title(), tuteename.title())

    msg.attach(MIMEText(msgintro))
    
    msg.attach(MIMEText('<a href = "https://forms.gle/RwMheLT4W7k9Xg8u7">Session Feedback Survey</a>','html'))

    #spacer
    msg.attach(MIMEText('\n\n============================================================================================\n\n'))

    #tutorname
    msg.attach(MIMEText('Tutor Name: ' + tutorname.title() + '\n\n'))
    #the summary
    msg.attach(MIMEText('Topics Covered with Tutor (written by Tutor): \n' + summary + '\n\n')) #attach a text object to ontain the text
    #the summary
    msg.attach(MIMEText('Suggested Homework (written by Tutor): \n' + suggestions + '\n\n'))

    #second spacer
    msg.attach(MIMEText('============================================================================================\n\n'))

    msgoutro = '''
We hope to see you soon,

The Merry Tutor

'''

    imgtext = MIMEText('<img src="cid:image1" style="width:125px;height:125px;">', 'html')
    msg.attach(imgtext)

    image = MIMEImage(open('app/static/RoundLogo.png', 'rb').read())

    msg.attach(MIMEText('\nInstagram: https://www.instagram.com/themerrytutor/?hl=en' + 
                        '\nTwitter: https://twitter.com/themerrytutor' + 
                        '\nWebsite: https://themerrytutor.org'))

    # Define the image's ID as referenced in the HTML body above
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    to = [email]
    smtp.sendmail(from_addr="naperville.themerrytutor@gmail.com",
                to_addrs=to, msg=msg.as_string())

    smtp.quit() #terminate connection