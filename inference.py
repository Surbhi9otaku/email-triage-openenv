import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

print("[START]")

try:
    r = requests.post(f"{BASE_URL}/reset")
    print("[STEP] reset:", r.json())

    for i in range(3):
        r = requests.post(f"{BASE_URL}/step", json={"action": "correct"})
        print("[STEP]", r.json())

except Exception as e:
    print("[ERROR]", str(e))

print("[END]")