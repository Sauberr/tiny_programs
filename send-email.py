import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(Path('templates/index.html').read_text())
html_content = html_template.substitute({'name': 'Dima', 'date': 'tomorrow'})

my_email['from'] = 'Dima'
my_email['to'] = 'sauberrtest@gmail.com'
my_email['subject'] = 'Hello from Dima'
my_email.set_content(html_content, 'html')

with open('images/mail-download.gif', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='gif', filename='mail-downland.gif')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls() encryption if you want
    # smtp_server.login('username', 'password') for login if you want
    smtp_server.send_message(my_email)
    print('Email was sent!')
