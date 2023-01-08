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
* - variables not nessisary to fill in if using defaults specified

import SnailMail as sm
sm.makeSignIn(email, passw, fname) - Make a New Sign In 
sm.sendEmail(signIn, emailTo, subject, body, *imapServ, *imapPort)
sm.getEmails(signIn, selCrit='Inbox', *imapServ, *imapPort)  
sm.searchEmails(signIn,  search,  *searchCrit, *selInbox,*imapServ, *imapPort)
sm.delEmails(signIn,  search,  *searchCrit, *selInbox, *imapServ, *imapPort)
  email - Email used (string)
  passw - Password Token (Not email password)
  fname - assgined string for signIn ('mysignin')
  signIn - same as fname
  emailTo - email address asstring to send email to ('exampleuser@website.com')
  subject - subject line of email
  body - body of email
  *searchCrit - type sm.helpCrit() when using for more info (Default 'BODY')
  *selInbox - which inbox to use (default '"[Gmail]/All Mail"')
  *imapServ - SMTP Server Address(default google SMTP server)
  *imapPort - SMTP Server Port (default google SMTP port)
  
