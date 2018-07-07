import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "fromaddress"
toaddr = ['toaddress'] 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "second attachment test"
msg['cc']="hello messages"
 
body = "this is the message and the attachment through the python code"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "file access method.docx"
attachment = open("your attachment", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "your_password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
 
