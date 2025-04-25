import requests
import time

URL = "http://localhost:5000/notify"
API_KEY = "supersecretapikey123"  # 🔑 Replace with the actual API key

headers = {
    "Content-Type": "application/json",
    "X-API-KEY": API_KEY
}

payload = {
    "event_type": "user_registered",
    "payload": {
        "name": "Lokesh Test User",
        "email": "lokeshd4ngi@gmail.com"
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
