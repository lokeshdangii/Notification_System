from channels.email_channel import EmailChannel
from logging_config import setup_logger

logger = setup_logger()

class NotificationDispatcher:
    def __init__(self, config):
        self.email_channel = EmailChannel(config)

    def dispatch(self, event_type, payload):
        if event_type == "user_registered":
            subject = "Welcome to Notify!"
            body = f"<p>Hello {payload['name']}, thanks for registering.</p>"
            logger.info(f"Dispatching user_registered event to {payload['email']}")
            return self.email_channel.send(payload["email"], subject, body)
        logger.warning(f"Unhandled event type: {event_type}")
        return False
