#  Security Automation Dashboard

A lightweight, demo-grade **Security Orchestration & Automated Response (SOAR) dashboard**.  
This project visually simulates a SOC automation system while remaining extremely simple under the hood.

Perfect for CISOs, Security Engineers, and DevSecOps leaders who want a professional, executive-level technical project.

---

##  Features

- Fake but realistic security alerts (JSON-backed)
- Click-to-run automation workflows
- Simple backend workflow engine
- Dashboard UI using FastAPI + HTML/JS
- Looks like an enterprise SOC tool

---
## How to install and use

### pip
```pip install -r requirements.txt
uvicorn src.app:app --reload
```
---
### uv
```uv add -r requirements.txt
uv run uvicorn src.app:app --reload

```

##  Architecture Diagram

```mermaid
flowchart TD
    A[Alerts JSON] --> C(Dashboard UI)
    B[Workflows JSON] --> C
    C --> D[FastAPI Backend]
    D --> E[Workflow Engine]
    E --> F[Execution Log]

