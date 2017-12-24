# Requirements
# Check if site is working
# If site is not working take a screen shot of the page
# Include a timestamp in the screen shot
# Email the screen shot

from selenium import webdriver  # allows for driving a browser as a user
from smtplib import SMTP        # allows for sending of emails
from PythonScripts.webpageTestTool.config import *  # allows for using data stored externally from the script
from email.mime.base import MIMEBase  # base class for all the MIME-specific subclasses
from email.mime.text import MIMEText  # allows for creation of MIME objects
from email.mime.multipart import MIMEMultipart  # subclass of MIMEBase; allows for attaching part to a message
from email.encoders import encode_base64  # encodes data for transport; default is base64


def get_screen_shot():
    browser = webdriver.Firefox()  # specify Firefox as the browser of choice
    # browser.get('http://www.zuzustutus.com')
    browser.get('http://www.python.org')  # GET call
    # assert "ZuZu's TuTus" in browser.title  # Validates target
    browser.save_screenshot('screenshots.png')  # takes a screen shot of the page
    browser.quit()  # close out browser


def email_screen_shot():
    email_to
    email_from
    email_cc
    subject = 'Site Status Check By Python!'

    msg = MIMEMultipart()  # creating a msg object
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Cc'] = email_cc
    msg['Subject'] = subject

    # This is the actual message being sent
    body = 'Hi, \n\n' \
           'Here is a screen capture of your site. \n\n' \
           'Sent by Python Bot!'
    msg.attach(MIMEText(body, 'plain'))  # attaching the body to the msg object defined above

    filename = 'screenshots.png'
    attachment = open(filename, 'rb')  # read file in binary

    # setting up parts of the attachment
    part = MIMEBase('application', 'octet-stream')  # using streams to upload the attachment
    part.set_payload(attachment.read())
    encode_base64(part)  # encode the attachment to base64
    part.add_header('Content-Disposition', 'attachment; filename=' + filename)  # specify what's being sent

    msg.attach(part)  # attach attachment to the msg object
    text = msg.as_string()

    # setting up connection with an SMTP server
    server = SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(username, password)

    # sending email
    server.sendmail(email_from, email_to, text)
    server.quit()


get_screen_shot()
email_screen_shot()

