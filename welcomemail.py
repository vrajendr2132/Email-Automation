#!/usr/bin/python

__author__ = "Vineeth Rajendran Sreenivasan"
__version__ = "1.0.0"
__email__ = "vinu.rs24@gmail.com"
__Created__ = "20/07/2022"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'xyz@gmail.com'
receivers1 = ['abc@gmail.com']
receivers2 = ['cde@gmail.com']

msg = MIMEMultipart('alternative')
msg['Subject'] = "Redspam Passback"
msg['From'] = sender
msg['To'] = ", ".join(receivers1)
msg['Cc'] = ", ".join(receivers2)


message = """
<body><p>Hello Redspam,</p>

<p><div>Hello World!!!!.</div></p>
</p>Welcome to our Organization.</p></body>


<body><p><b><div><br>Regards,</br></div></b></p>
<p><b><div>Connectivity Services,NOC</div></b></p>
<p><b><div>RM Education</div></b></p></body>

"""



print (message)

text = "Welcome mail"
part1 = MIMEText(text, 'plain')
part2 = MIMEText(message,'html')
msg.attach(part1)
msg.attach(part2)
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com')
   smtpObj.sendmail(sender, receivers1+receivers2, msg.as_string())
   #smtpObj.sendmail(sender, receivers1, msg.as_string())
   print "Successfully sent email"
   smtpObj.quit()
except Exception, e:
   str(e)
   print "Error: unable to send email"

