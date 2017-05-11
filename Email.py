import smtplib
import os
sender = 'noah.darian@gmail.com'
receivers = ['colsonse@gmail.com']


def sendmail(receivers):
   if receivers is None:
      receivers = ['colsonse@gmail.com']
   
   extramessage = open('list.txt', 'r')
   message = """From: Your personal Raspberry pi
   To: To Person <colsam@warroad.k12.mn.us>
   Subject: Shopping List
   """ + extramessage.read() + """

      Thank you!"""
   try:
      print "attempting connection"
      server = smtplib.SMTP('smtp.googlemail.com', 587)
      print "connected!"
      server.starttls()
      print "attempting..."
      server.login(sender, 'Reach(!$')
      print "Login successful"
      server.sendmail(sender, receivers, message)
      server.quit()
      print "Successfully sent email"
   except smtplib.SMTPRecipientsRefused:
      print "Rejected"
      return
   except smtplib.SMTPException as e:
      print "Error: unable to send email" + e.smtp_error
