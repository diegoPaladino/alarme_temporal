#link of tutorial: https://www.youtube.com/watch?v=sXjpkcF7rPQ
# #Joining the content of the some previous test (https://www.youtube.com/watch?v=JRCJ6RtE3xU) with this tutorial, was sucess!
#password='paladino804680'

import smtplib

sender_email= "diegopaladinofoto@gmail.com"
rec_email="diegopaladinoemfrc@gmail.com"
password='Paladio804680'
#message=" texto 0123456789"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)

subject = 'PONTO DIEGO'
body = 'SAIDA: 18:00'

msg = f'Subject: {subject}\n\n{body}'

print("Login succes")
server.sendmail(sender_email,rec_email,msg)
print("Email has sent to",rec_email)

