import sys
import smtplib

fromAddress = "pdt-waiting@mit.edu"
subject = "Waiting Duty"
toAddress = sys.argv[1]
msg = """
Yo Bro,

Do your waiting duty today.
"""

def email(to_addr, from_addr, subject, msg):
    smtpserver = smtplib.SMTP("outgoing.mit.edu")
    header = 'To:' + to_addr + '\n' + 'From:' + from_addr + '\n' + 'Subject: ' + subject + '\n'
    message = header + '\n' + message
    smtpserver.sendmail(from_addr, to_addr, message)
    smtpserver.close()


email(toAddress, fromAddress, subject, msg)
