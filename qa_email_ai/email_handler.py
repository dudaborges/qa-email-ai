import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from imbox import Imbox

load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
HOST = 'imap.gmail.com'
USERNAME = os.getenv('EMAIL_USERNAME')
PASSWORD = os.getenv('EMAIL_PASSWORD')

start_date = datetime(2025, 1, 22)
email_sender = 'duda.pborges92@gmail.com'


def get_emails():
    emails = []

    with Imbox(HOST, username=USERNAME, password=PASSWORD) as imbox:
        unread_messages = imbox.messages(
            unread=True, date__gt=start_date, sent_from=email_sender
        )

        for uid, message in unread_messages:
            name = message.sent_from[0]['name']
            email = message.sent_from[0]['email']
            subject = message.subject
            body = message.body['plain'][0]

            email = {
                'id': uid,
                'name': name,
                'email': email,
                'subject': subject,
                'body': body,
            }

            emails.append(email)

    return emails


def send_email(to_email, subject, body):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)

            msg = MIMEMultipart()
            msg['From'] = USERNAME
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server.send_message(msg)
            print(f'E-mail enviado com sucesso para {to_email}')
    except Exception as e:
        print(f'[ERROR] Error sending email to {to_email}: {e}')
