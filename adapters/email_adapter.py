# adapters/email_adapter.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAdapter:
    def __init__(self, smtp_user, smtp_pass, smtp_server, smtp_port):
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, sender, recipient, subject, body):
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
                server.sendmail(sender, recipient, msg.as_string())
            print(f"[✔] Email successfully sent to {recipient}")
            return True
        except Exception as e:
            print(f"[✖] Failed to send email to {recipient}: {e}")
            return False
