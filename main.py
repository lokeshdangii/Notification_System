# main.py
from dispatcher import NotificationDispatcher
from config import CONFIG

dispatcher = NotificationDispatcher(CONFIG)

# Simulated trigger
event_payload = {
    "name": "Lokesh Dangi",
    "email": "lokeshd4ngi@gmail.com"
}

result = dispatcher.dispatch("user_registered", event_payload)

if result:
    print("[✅] Notification dispatched successfully.")
else:
    print("[❌] Notification dispatch failed.")
