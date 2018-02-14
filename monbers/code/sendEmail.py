from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage
import smtplib

attachment = 'image.jpg'

msg = MIMEMultipart()
msg["To"] = "angerhangy@gmail.com"
msg["From"] = "hi"
msg["Subject"] = "i don'tk now"


fp = open(attachment, 'rb')
msgText = MIMEImage(fp.read())
msg.attach(msgText)   # Added, and edited the previous line

fp = open(attachment, 'rb')                                                    
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

print (msg.as_string())

## send email
mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('angerhangy@gmail.com', 'ANGERhang0601')

mailserver.sendmail('angerhangy@gmail.com','hang.yuan@epfl.ch', msg.as_string())

mailserver.quit()