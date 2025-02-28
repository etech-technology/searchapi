from fastapi import FastAPI, HTTPException
import requests
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Simulated name database
NAMES_DB = {"john": "John Doe", "jane": "Jane Smith", "alice": "Alice Johnson", "elvis": "Etech Devops"}

PAGERDUTY_ROUTING_KEY = os.getenv("PAGERDUTY_ROUTING_KEY")
PAGERDUTY_API_URL = "https://events.pagerduty.com/v2/enqueue"

def trigger_pagerduty_alert(name: str):
    if not PAGERDUTY_ROUTING_KEY:
        print("PagerDuty routing key not set. Skipping alert.")
        return
    
    payload = {
        "routing_key": PAGERDUTY_ROUTING_KEY,
        "event_action": "trigger",
        "payload": {
            "summary": f"Name check request for {name}",
            "severity": "info",
            "source": "search-api"
        }
    }
    try:
        response = requests.post(PAGERDUTY_API_URL, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to trigger PagerDuty alert: {e}")

@app.get("/search")
def search_name(name: str):
    if name.lower() in NAMES_DB:
        trigger_pagerduty_alert(name)
        return {"name": NAMES_DB[name.lower()]}
    raise HTTPException(status_code=404, detail="Name not found")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
