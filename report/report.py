import smtplib
import logging
import datetime
from email.mime.text import MIMEText as text


class Report:
    logger = logging.getLogger(__name__)
    body = ""

    def __init__(self, email_address_sender, password, email_recipient):
        self.email_address_sender = email_address_sender
        self.password = password
        self.email_recipient = email_recipient
        self.body += "BITTREX ANALYTICS - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

    def add(self, title, message):
        """
        :return: Adding text to Message
        """
        self.body += "\n\n" + title.upper() + "\n" + message

    def send(self):
        """
        Sends message email
        """
        self.logger.info("Sending email..")
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(self.email_address_sender, self.password)

        msg = text(self.body)
        msg['Subject'] = "Bittrex - Analytics"
        msg['From'] = self.email_address_sender
        msg['To'] = self.email_recipient

        smtp_server.sendmail(self.email_address_sender, self.email_recipient, msg.as_string())
        smtp_server.quit()
        self.logger.info("Sending email - done")
