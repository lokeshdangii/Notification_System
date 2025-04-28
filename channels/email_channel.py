# channels/email_channel.py

from adapters.email_adapter import EmailAdapter
from logging_config import logger  

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
        logger.info(f"[EmailChannel] Sending email to {recipient} with subject '{subject}'")
        result = self.adapter.send_email(self.sender, recipient, subject, body)
        
        if result:
            logger.info(f"[EmailChannel] Email successfully sent to {recipient}")
        else:
            logger.error(f"[EmailChannel] Failed to send email to {recipient}")
        
        return result
