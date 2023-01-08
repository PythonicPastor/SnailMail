# SnailMail
A module that simplifies the usage of the imap module for the purpose of sending, reading, searching, and deleteing emails right from the python console

please note that you need to make a sign in file using SnailMail.makeSignIn('email', 'passwordToken', 'filename')

To get the password token simply Go to your Google account -> security -> App Password under "Signing in to google".

If you dont see the App passwords button turn on two-step verification.

1.Create a new App.

2.Under "Select App" select "Other" and type in "Python"

3.Copy the password.

and you should be ready to use SnailMail(assuming your using google)

Commands:
import SnailMail as sm
sm.makeSignIn(email, passw, fname) - Make a New Sign In 

sm.sendEmail(signIn, emailTo, subject, body, *smtpServ, *smtpPort)
  signIn - file name as string for signIn (.json not needed)
  emailTo - email your sending to as string
  subject - subject line of email
  body - the actual email content
  smtpServ - SMTP server (google Default)
  smtpPort - SMTP port (google Default)
  
getEmails(fname, selCrit='Inbox', *imapServ, *imapPort)
  
  
