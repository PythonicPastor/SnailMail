from email.message import EmailMessage
import ssl
import smtplib
import imaplib
import email
import json

def makeSignIn(email, passw, fname):
    aList = {'email':email, 'password':passw}
    jsonStr = json.dumps(aList)
    jsonFile = open(fname +".json", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

def loadSignIn(user):
    fileObject = open(user +".json", "r")
    jsonContent = fileObject.read()
    bList = json.loads(jsonContent)
    return (bList['email'], bList['password'])

def sendEmail(signIn, emailTo, subject, body, imapServ = 'smtp.gmail.com', imapPort=465):
    emailFrom, passw = loadSignIn(signIn)
    em = EmailMessage()
    em['From'] = emailFrom
    em['To']= emailTo
    em['subject'] = subject
    em.set_content(f"""{body}""")

    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(smtpServ, smtpPort, context=context) as smtp:
        smtp.login(emailFrom, passw)
        smtp.sendmail(emailFrom, emailTo, em.as_string())
        
def getEmails(fname, selCrit='Inbox',imapServ='imap.gmail.com', imapPort = '993'):
    emailAdd, passw = loadSignIn(fname)
    imap = imaplib.IMAP4_SSL(imapServ)

    imap.login(emailAdd, passw)
    imap.select(selCrit)

    _, msgNums = imap.search(None, 'ALL')

    rcvEmails = {}

    for msgnum in msgNums[0].split():
        _, data = imap.fetch(msgnum, '(RFC822)')

        message = email.message_from_bytes(data[0][1])

        msgPart = ''
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                msgPart += part.as_string()
        rcvEmails[str(msgnum)] = {
                     'MsgFrom' :    str(message.get('From')),
                     'MsgTo' :        str(message.get('To')),
                     'MsgBCC' :     str(message.get('BCC')),
                     'MsgDate' :    str(message.get('Date')),
                     'MsgSubj' :    str(message.get('Subject')),
                     'Msg' : msgPart
                     }
    imap.close
    return json.dumps(rcvEmails, indent = 4)

def searchEmails(signIn,  search,  searchCrit ='BODY', selInbox='"[Gmail]/All Mail"',imapServ='imap.gmail.com', imapPort = '993'):
    emailAdd, passw = loadSignIn(signIn)
    imap = imaplib.IMAP4_SSL(imapServ)

    imap.login(emailAdd, passw)
    imap.select(selInbox)

    res , msgNums = imap.search(None, f'{searchCrit}', f'"{search}"')

    rcvEmails = {}

    for msgnum in msgNums[0].split():
        _, data = imap.fetch(msgnum, '(RFC822)')

        message = email.message_from_bytes(data[0][1])

        msgPart = ''
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                msgPart += part.as_string()
        rcvEmails[str(msgnum)] = {
                     'MsgFrom' :    str(message.get('From')),
                     'MsgTo' :        str(message.get('To')),
                     'MsgBCC' :     str(message.get('BCC')),
                     'MsgDate' :    str(message.get('Date')),
                     'MsgSubj' :    str(message.get('Subject')),
                     'Msg' : msgPart
                     }
    imap.close
    return json.dumps(rcvEmails, indent = 4) 

def delEmails(signIn,  search,  searchCrit ='BODY', selInbox='"[Gmail]/All Mail"',imapServ='imap.gmail.com', imapPort = '993'):
    emailAdd, passw = loadSignIn(signIn)
    imap = imaplib.IMAP4_SSL(imapServ)

    imap.login(emailAdd, passw)
    imap.select(selInbox)

    res , msgNums = imap.search(None, f'{searchCrit}', f'"{search}"')

    for msgnum in msgNums[0].split():
        imap.store(msgnum, '+X-GM-LABELS', '\\Trash')
        print(msgnum)
        
def  helpCrit():

    print('ALL - return all messages matching the rest of the criteria \n\
    ANSWERED - match messages with the \\ANSWERED flag set \n\
    BCC "string" - match messages with "string" in the Bcc: field \n\
    BEFORE "date" - match messages with Date: before "date" \n\
    BODY "string" - match messages with "string" in the body of the message\n\
    CC "string" - match messages with "string" in the Cc: field\n\
    DELETED - match deleted messages\n\
    FLAGGED - match messages with the \\FLAGGED (sometimes referred to as Important or Urgent) flag set\n\
    FROM "string" - match messages with "string" in the From: field\n\
    KEYWORD "string" - match messages with "string" as a keyword\n\
    NEW - match new messages\n\
    OLD - match old messages\n\
    ON "date" - match messages with Date: matching "date"\n\
    RECENT - match messages with the \\RECENT flag set\n\
    SEEN - match messages that have been read (the \\SEEN flag is set)\n\
    SINCE "date" - match messages with Date: after "date"\n\
    SUBJECT "string" - match messages with "string" in the Subject:\n\
    TEXT "string" - match messages with text "string"\n\
    TO "string" - match messages with "string" in the To:\n\
    UNANSWERED - match messages that have not been answered\n\
    UNDELETED - match messages that are not deleted\n\
    UNFLAGGED - match messages that are not flagged\n\
    UNKEYWORD "string" - match messages that do not have the keyword "string"\n\
    UNSEEN - match messages which have not been read yet'
    )
