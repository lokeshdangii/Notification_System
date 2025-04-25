from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dispatcher import NotificationDispatcher
from config import CONFIG

app = Flask(__name__)
dispatcher = NotificationDispatcher(CONFIG)

# ✅ Get API key from config
API_KEY = CONFIG["API_KEY"]

@app.route('/notify', methods=['POST'])
def notify():
    # 🔐 Check for API key in header
    client_api_key = request.headers.get("X-API-KEY")
    if client_api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    event_type = data.get("event_type")
    payload = data.get("payload")

    if not event_type or not payload:
        return jsonify({"error": "Missing event_type or payload"}), 400

    result = dispatcher.dispatch(event_type, payload)

    if result:
        return jsonify({"message": "Notification sent successfully"}), 200
    else:
        return jsonify({"message": "Failed to send notification"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
