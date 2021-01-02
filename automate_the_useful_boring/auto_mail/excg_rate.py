#!python 3
# simple experiment of sending a mail with time info
import smtplib, datetime
from retrievejson import exchg_rate
import SMTP

MAIL_ADDR = 'foo@gmail.com'
pw = input('Enter your password:')
smtpObj=SMTP.mail_login(pw, MAIL_ADDR)

#sending the time
# SUBJECT = 'The current time is '+ datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
# TEXT = 'May the Force be with you. Sincerely, Jon from the past'
# msg = mail_msg(SUBJECT, TEXT)

rate = exchg_rate('USD', 'JPY')[2]
msg = SMTP.mail_msg('Exchange Rate','The exchange rate for USD/JPY is '+ str(rate))
print('Sending Exchange Rate....')
smtpObj.sendmail('foo@gmail.com','foo@gmail.com',msg)

smtpObj.quit()