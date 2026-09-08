from agents.base import BaseAgent

class PersonalizationAgent(BaseAgent):
    name = "personalization"
    def execute(self, task):
        return f"Kişiselleştirme isteği işlendi; kalıcı hafızaya yalnızca uygun bilgiler alınmalıdır. Görev: {task}"
