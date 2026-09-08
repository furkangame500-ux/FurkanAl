from core.agent_manager import AgentManager
from core.security import SecurityManager
from memory.store import MemoryStore
from core.models import TaskRequest

class Orchestrator:
    def __init__(self):
        self.agent_manager = AgentManager()
        self.security = SecurityManager()
        self.memory = MemoryStore()

    def route(self, message: str):
        m = message.lower()
        routes = []
        if any(x in m for x in ["araştır", "ara", "güncel", "kaynak", "internet"]):
            routes.append("research")
        if any(x in m for x in ["kod", "python", "program", "bug", "yazılım", "github"]):
            routes.append("coding")
        if any(x in m for x in ["görsel", "resim", "logo", "thumbnail", "video"]):
            routes.append("media")
        if any(x in m for x in ["hatırla", "unut", "tercih", "benim"]):
            routes.append("personalization")
        if any(x in m for x in ["duygu", "ton", "ciddi", "eğlenceli"]):
            routes.append("emotion")
        if any(x in m for x in ["derin araştır", "karşılaştır", "kapsamlı"]):
            routes.append("deep_research")
        if any(x in m for x in ["geliştir", "optimize", "iyileştir", "test et"]):
            routes.append("self_improvement")
        return routes or ["general"]

    def handle(self, req: TaskRequest):
        agents = self.route(req.message)
        results = []
        for name in agents:
            if name == "general":
                results.append({"agent": "orchestrator", "success": True, "output": "Görev genel amaçlı olarak alındı."})
            else:
                results.append(self.agent_manager.run(name, req.message, req.autonomy_level))
        return {
            "task": req.message,
            "selected_agents": agents,
            "results": results,
            "note": "Gerçek dış sistem işlemleri için araç adapterları ve izin kontrolü uygulanmalıdır."
        }
