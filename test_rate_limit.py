import requests
import time
import os

URL = "http://54.85.143.45:5000/notify"
API_KEY = os.environ.get("API_KEY")

headers = {
    "Content-Type": "application/json",
    "X-API-KEY": API_KEY
}

payload = {
    "event_type": "order_confirmed",
    "payload": {
        "name": "Lokesh Test User",
        "email": "lokeshd4ngi@gmail.com",
        "order_id": "12345"
    }
}

# 🔁 Send multiple requests in a loop
for i in range(10):
    print(f"🔁 Sending request #{i + 1}")
    response = requests.post(URL, json=payload, headers=headers)
    print(f"🔙 Status Code: {response.status_code}")
    try:
        print(f"📦 Response: {response.json()}")
    except Exception:
        print("⚠️ Non-JSON response received")

    time.sleep(1)  # ⏱️ Adjust delay as needed (lower = likely to trigger rate limit)
