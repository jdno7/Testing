
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
# from email import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='jd@rodpowerindex.com',
    to_emails='jdhans@live.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)