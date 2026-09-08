from agents.base import BaseAgent

class ResearchAgent(BaseAgent):
    name = "research"
    def execute(self, task):
        return f"Research plan hazırlandı: kaynak bul → doğrula → karşılaştır → güven seviyesi ata. Görev: {task}"
