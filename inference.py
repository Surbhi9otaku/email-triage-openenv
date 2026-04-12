import requests

BASE_URL = "http://localhost:8000"

print("[START]")

r = requests.post(f"{BASE_URL}/reset")
print("[STEP] reset:", r.json())

for i in range(3):
    r = requests.post(f"{BASE_URL}/step", json={"action": "correct"})
    print("[STEP]", r.json())

print("[END]")