import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
password = user_pasword
s.login('user_name','{}'.format(password))
message = some_text
s.sendmail('username','recipient gmail', message)
s.quit()




