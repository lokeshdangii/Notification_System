# api/app.py

from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sys
import os

# 🔁 Path config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dispatcher import NotificationDispatcher
from logging_config import setup_logger
from config import CONFIG
from tasks import send_email_task  # ✅ Celery task import

# ✅ Setup logger
logger = setup_logger()

app = Flask(__name__)
dispatcher = NotificationDispatcher(CONFIG)

# 🔐 Load API key
API_KEY = CONFIG["API_KEY"]

# 🔐 Optional: Rate limit by API key instead of IP
def get_api_key():
    return request.headers.get("X-API-KEY") or get_remote_address()

# 🛡️ Setup Flask-Limiter
limiter = Limiter(
    key_func=get_api_key,  # 📌 Rate limit by API key
    default_limits=["10 per minute"]
)
limiter.init_app(app)

# ❗ Custom rate limit exceeded response
@app.errorhandler(429)
def ratelimit_handler(e):
    logger.warning(f"⚠️ Rate limit exceeded: {e.description}")
    return jsonify({
        "error": "Rate limit exceeded. Try again later.",
        "details": str(e.description)
    }), 429

@app.route('/notify', methods=['POST'])
@limiter.limit("5 per minute")  # 🔄 Specific limit for this route
def notify():
    logger.info("🔔 Received /notify request")

    # 🔐 API key check
    client_api_key = request.headers.get("X-API-KEY")
    if client_api_key != API_KEY:
        logger.warning("🚫 Unauthorized access attempt")
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    event_type = data.get("event_type")
    payload = data.get("payload")

    if not event_type or not payload:
        logger.error("❌ Missing event_type or payload in request")
        return jsonify({"error": "Missing event_type or payload"}), 400

    logger.info(f"📦 Processing event_type: {event_type} for email: {payload.get('email')}")

    if event_type == "user_registered":
        subject = "Welcome to Notify!"
        body = f"<p>Hello {payload['name']}, thanks for registering.</p>"

        try:
            send_email_task.delay(payload["email"], subject, body)
            logger.info(f"📨 Email task queued for {payload['email']}")
            return jsonify({"message": "Notification queued"}), 202
        except Exception as e:
            logger.exception(f"❌ Failed to queue email: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500

    logger.warning(f"⚠️ Unsupported event_type: {event_type}")
    return jsonify({"error": "Unsupported event type"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







# 💡 Optional: Rate limit by API Key (instead of IP) 

"""
def get_api_key():
    return request.headers.get("X-API-KEY", get_remote_address())

limiter = Limiter(
    app,
    key_func=get_api_key,
    default_limits=["10 per minute"]
)
"""