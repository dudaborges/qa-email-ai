import os
from dotenv import load_dotenv
from imbox import Imbox

load_dotenv()

HOST = 'imap.gmail.com'
USERNAME = os.getenv('EMAIL_USERNAME')
PASSWORD = os.getenv('EMAIL_PASSWORD')

with Imbox(HOST, username=USERNAME, password=PASSWORD) as imbox:
    unread_messages = imbox.messages(unread=True)

    for uid, message in unread_messages:
        print(f'De: {message.sent_from[0]}')
        print(f'Assunto: {message.subject}')
        print(f'Corpo: {message.body["plain"][0]}')
