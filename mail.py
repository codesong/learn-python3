#########################################################################
# File Name: mail.py
# Author: codesong
# mail: codesong@qq.com
# Created Time: 2016年09月15日 星期四 10时26分07秒
#########################################################################

#-*-coding:utf-8-*-

import smtplib
email_id = ['to@qq.com']
sender = 'from@qq.com'

receivers = email_id
yourname = 'Me'
recvname = email_id
sub = 'Sending email from Python'
body = 'Hey There!'

message = 'From:' + yourname + '\n'
message = message + 'Subject:' + sub + '\n'
message = message + body
server = smtplib.SMTP('smtp.qq.com:587')

username = sender
password = input('Type your password')
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(send, receivers, message)
server.quit()
print('sucessfully send!')



