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
