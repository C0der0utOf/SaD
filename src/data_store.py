import json

def get_alerts():
    with open("data/alerts.json", "r") as f:
        return json.load(f)

def get_workflows():
    with open("data/workflows.json", "r") as f:
        return json.load(f)

