import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CONFIG = {
    "SMTP_USER": os.getenv("SMTP_USER"),
    "SMTP_PASS": os.getenv("SMTP_PASS"),
    "SMTP_SERVER": os.getenv("SMTP_SERVER"),
    "SMTP_PORT": int(os.getenv("SMTP_PORT", 587)),  # Default to 587 if not found
    "EMAIL_SENDER": os.getenv("EMAIL_SENDER"),
    "API_KEY": os.getenv("API_KEY")
}


GOOGLE_CONFIG = {
    "SMTP_USER": "lokeshdangi1045@gmail.com",
    "SMTP_PASS": "mywf hxnw hnwv xvpw",
    "SMTP_SERVER": "smtp.gmail.com",
    "SMTP_PORT": 587,
}


MailGun_CONFIG = {
    "SMTP_USER": "lokesh@sandboxd63fecfaa40d4ed38af8bb26690159ec.mailgun.org",
    "SMTP_PASS": "Mailgun",
    "SMTP_SERVER": "smtp.mailgun.org",
    "SMTP_PORT": 587,
}

MailGun2_CONFIG = {
    "SMTP_USER": "postmaster@lokesh.dedyn.io",
    "SMTP_PASS": "Mailgun",
    "SMTP_SERVER": "smtp.mailgun.org",
    "SMTP_PORT": 587,
}