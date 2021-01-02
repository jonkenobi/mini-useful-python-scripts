#!python 3
# Basic helper codes to assist mail sending with SMTP. Can be imported by other programs for further use
# Simple experiment of sending a mail to my own mail account.
import smtplib

###---Helper Code also used in other programs
def mail_login(pw, account = 'foo@gmail.com'):
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com')
    smtpObj.ehlo()  #say hi to server
    # smtpObj.starttls()  start TLS
    smtpObj.login(account, pw)
    return smtpObj

def mail_msg(subject,text):
    # helper code to return a formatted string combining subject and text for use in the smtplib sendmail function.
    # Takes string parameters subject and text, and returns them in format.
    msg = 'Subject: {}\n\n{}'.format(subject, text)
    return msg

# SUBJECT = 'STAR WARS RULES'
# TEXT = 'May the Force be with you.'
#
# pw = input()
# test_smtpObj = mail_login(pw)
# msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
# test_smtpObj.sendmail('foo@gmail.com','foo@gmail.com',msg)
# test_smtpObj.quit()