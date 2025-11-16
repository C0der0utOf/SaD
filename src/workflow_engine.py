import json
from datetime import datetime

def run_workflow(workflow_id):
    with open("data/workflows.json", "r") as f:
        workflows = json.load(f)

    workflow = workflows.get(workflow_id)
    if not workflow:
        return {"error": "Workflow not found"}

    # Fake “steps” to simulate processing
    executed_steps = []
    for step in workflow["steps"]:
        executed_steps.append({
            "step": step,
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        })

    return {
        "workflow": workflow["name"],
        "executed": executed_steps
    }

