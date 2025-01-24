from email_handler import get_emails, send_email
from llm import generate_response


def reply_to_emails():
    emails = get_emails()

    for email in emails:
        name = email['name']
        subject = email['subject']
        body = email['body']

        print(f'Nome: {name} \nAssunto: {subject} \nCorpo: {body}')
        print(f'{"-"*50}')

        to_email = email['email']
        reply_subject = f'Re: {subject}'
        reply_body = generate_response(name=name, subject=subject, body=body)

        send_email(to_email, reply_subject, reply_body)


reply_to_emails()
