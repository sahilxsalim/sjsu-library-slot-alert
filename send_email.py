import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(message):
    message = Mail(
        from_email='sahilsalim1999@gmail.com',
        to_emails='6506707856@txt.att.net',
        subject='New Slots Available',
        # html_content=f'<h1><strong>{message}</strong></h1>')
        plain_text_content=message)

    # with open('Visa_Status.png', 'rb') as f:
    #     data = f.read()
    #     encoded_data = base64.b64encode(data).decode()
    #     image_attachment = Attachment(
    #         FileContent(encoded_data),
    #         FileName('Visa_Status.png'),
    #         FileType('image/png'),
    #         Disposition('attachment')
    #     )
    #     message.attachment = image_attachment
    try:
        sg = SendGridAPIClient(
            os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print("EMAIL SENT", response)
    except Exception as e:
        print(e.message)
