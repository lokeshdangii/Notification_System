# logger.py
import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name="notification_logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # ✅ Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ✅ Rotating File handler for all logs
    general_log_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=5*1024*1024, backupCount=3  # 5MB, 3 backups
    )
    general_log_handler.setFormatter(formatter)
    general_log_handler.setLevel(logging.INFO)
    logger.addHandler(general_log_handler)

    # ✅ Separate Rotating File handler for errors only
    error_log_handler = RotatingFileHandler(
        "logs/error.log", maxBytes=2*1024*1024, backupCount=3  # 2MB, 3 backups
    )
    error_log_handler.setFormatter(formatter)
    error_log_handler.setLevel(logging.ERROR)
    logger.addHandler(error_log_handler)

    return logger
