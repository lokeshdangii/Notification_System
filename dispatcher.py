# dispatcher.py
from channels.email_channel import EmailChannel

class NotificationDispatcher:
    def __init__(self, config):
        self.email_channel = EmailChannel(config)

    def dispatch(self, event_type, payload):
        if event_type == "user_registered":
            subject = "Welcome to Notify!"
            body = f"<p>Hello {payload['name']}, thanks for registering.</p>"
            return self.email_channel.send(payload["email"], subject, body)
        return False
