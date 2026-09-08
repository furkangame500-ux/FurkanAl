from agents.base import BaseAgent

class CodingAgent(BaseAgent):
    name = "coding"
    def execute(self, task):
        return f"Kod görevi analiz edildi. Güvenli akış: analiz → sandbox/test → güvenlik kontrolü → uygulama. Görev: {task}"
