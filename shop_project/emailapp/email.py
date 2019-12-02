import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Eamil:
    @staticmethod
    def sendSignUpConfirmation(request, to_username, to_user_email):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Account succesfully created"
        msg["From"] = "087richard087@gmail.com"
        msg["Date"] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        html = """<html><body><h2><Account has been created!
        Account Name: {}</h2></body></html>""".format(to_username)
        content - MIMEText(html, "html")
        msg.attach(content)
        Email.send_email(to_user_email, msg)

    @staticmethod
    def send_email(request, message):
        port = 25
        smtp_server = "localhost"
        sender_email = "087richard087@gmail.com"
        server = smtplib.SMTP(smtp_server)
        server.sendmail("andrei.istrate2014@yahoo.com", str(request), message.as_string())