# channels/email_channel.py
from adapters.email_adapter import EmailAdapter

class EmailChannel:
    def __init__(self, config):
        self.adapter = EmailAdapter(
            config["SMTP_USER"],
            config["SMTP_PASS"],
            config["SMTP_SERVER"],
            config["SMTP_PORT"]
        )
        self.sender = config["EMAIL_SENDER"]

    def send(self, recipient, subject, body):
        return self.adapter.send_email(self.sender, recipient, subject, body)
