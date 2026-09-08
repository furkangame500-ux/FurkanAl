from core.orchestrator import Orchestrator
from core.models import TaskRequest

def test_router():
    o = Orchestrator()
    assert "research" in o.route("internetten güncel bilgi araştır")

def test_coding_router():
    o = Orchestrator()
    assert "coding" in o.route("python kodu yaz")
