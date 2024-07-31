import imaplib
import smtplib
from email.mime.text import MIMEText

def read_email(imap_server, imap_username, imap_password):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(imap_username, imap_password)
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    for num in messages[0].split():
        status, msg = mail.fetch(num, '(RFC822)')
        raw_message = msg[0][1]
        # Parse the raw message using email.parser
        print(raw_message)

def send_email(smtp_server, smtp_username, smtp_password, recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = recipient
    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, recipient, msg.as_string())
    server.quit()

# Example usage:
imap_server = "imap.gmail.com"
imap_username = "your_email@gmail.com"
imap_password = "your_email_password"
read_email(imap_server, imap_username, imap_password)

smtp_server = "smtp.gmail.com"
smtp_username = "your_email@gmail.com"
smtp_password = "your_email_password"
recipient = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent using Python."
send_email(smtp_server, smtp_username, smtp_password, recipient, subject, body)