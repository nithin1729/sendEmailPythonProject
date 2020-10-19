import smtplib

sender_email = "munaganithin.mnk@gmail.com"
password = "Your Password" ##You need to provide your password
rec_email = "munaganithin.mnk@gmail.com"
message = "Hi, I am Nithin. Sending this email using Python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email,rec_email,message)
print("Email has been sent to ", rec_email)