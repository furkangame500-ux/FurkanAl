from fastapi import FastAPI
from core.orchestrator import Orchestrator
from core.models import TaskRequest

app = FastAPI(title="FurkanAl", version="0.1.0")
orchestrator = Orchestrator()

@app.get("/")
def root():
    return {"name": "FurkanAl", "status": "online"}

@app.get("/health")
def health():
    return {"status": "ok", "agents": orchestrator.agent_manager.list_agents()}

@app.post("/task")
def task(req: TaskRequest):
    return orchestrator.handle(req)

@app.get("/memory")
def memory():
    return orchestrator.memory.list_recent()

@app.get("/security/policies")
def policies():
    return orchestrator.security.list_policies()
