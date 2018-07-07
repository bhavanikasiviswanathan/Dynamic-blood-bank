import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "bavanithanjavur@gmail.com"
toaddr = ['rabinayasep@gmail.com'] 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "second attachment test"
msg['cc']="hello messages"
 
body = "this is the message and the attachment through the python code"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "file access method.docx"
attachment = open("/home/bhavani/Documents/study/sem4/os/unit - 4/file access method.docx", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "indra BHAVANI5")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
 