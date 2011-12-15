import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

def SendMail(gmail_user, gmail_name, gmail_pwd, to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_name
   msg['To'] = to
   msg['Subject'] = subject
   msg.attach(MIMEText(text))
   if (attach != ""):      
      # Attach the file
      part = MIMEBase('application', 'octet-stream')
      part.set_payload(open(attach, 'rb').read())
      Encoders.encode_base64(part)
      part.add_header('Content-Disposition',
	      'attachment; filename="%s"' % os.path.basename(attach)) 
      msg.attach(part)
      
   try:
      mailServer = smtplib.SMTP("smtp.gmail.com", 587)
      mailServer.ehlo()
      mailServer.starttls()
      mailServer.ehlo()
      mailServer.login(gmail_user, gmail_pwd)
   except smtplib.SMTPAuthenticationError:
	 return "Error in Authentication"
   try:  
      mailServer.sendmail(gmail_name, to, msg.as_string())  
   except smtplib.SMTPAuthenticationError: # More detailed exception catching to be impplimented
      return "Error Sending mail"
   finally:  
      #mailServer.close() 
      mailServer.quit()

if __name__ == "__main__": # This is not needed as this file is used as a module. Just having it in case I decide to do anything with it in the future
      pass 
      
