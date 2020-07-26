import smtplib
from email.message import EmailMessage
import imghdr
import urllib.request

bot='gildiscordbot@gmail.com'
EMAIL_ADDRESS = bot
EMAIL_PASSWORD = 'qppcxazktetownat'

contacts = [bot]

def send(subject, body, attachment=[]):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content(body)
    for i in attachment:
        urllib.request.urlretrieve(i, "sample.png")
        with open("sample.png", 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image',
                           subtype=imghdr.what(None, img_data))   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
