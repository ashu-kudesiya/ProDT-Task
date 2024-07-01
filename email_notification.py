import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')  # Retrieve SendGrid API key from environment variable

def send_email(recipient, subject, content):
    """
    Sends an email using SendGrid API.

    Args:
        recipient (str): Email address of the recipient.
        subject (str): Subject line of the email.
        content (str): Content/body of the email.
    """
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email("ashu.kudesiya@gmail.com")  # Replace with your sender email
    to_email = To(recipient)
    content = Content("text/plain", content)
    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        print(f"Email sent to {recipient}, status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")
