# tasks.py

from celery_app import celery
from channels.email_channel import EmailChannel
from config import CONFIG
from logging_config import setup_logger

logger = setup_logger()
email_channel = EmailChannel(CONFIG)

@celery.task
def send_email_task(email, subject, body):
    logger.info(f"[Task] Triggered send_email_task for {email}")
    try:
        result = email_channel.send(email, subject, body)
        if result:
            logger.info(f"[Task] Email successfully sent to {email}")
        else:
            logger.error(f"[Task] Failed to send email to {email}")
        return result
    except Exception as e:
        logger.exception(f"[Task] Exception while sending email to {email}: {str(e)}")
        return False
