from agents.base import BaseAgent

class MediaAgent(BaseAgent):
    name = "media"
    def execute(self, task):
        return f"Medya görevi planlandı; görsel/video üretim adapterı bağlanabilir. Görev: {task}"
