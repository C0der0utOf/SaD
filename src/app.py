from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .workflow_engine import run_workflow
from .data_store import get_alerts, get_workflows

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    alerts = get_alerts()
    workflows = get_workflows()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "alerts": alerts,
        "workflows": workflows
    })

@app.post("/run/{workflow_id}")
def execute_workflow(workflow_id: str):
    result = run_workflow(workflow_id)
    return {"status": "ok", "workflow_id": workflow_id, "result": result}

