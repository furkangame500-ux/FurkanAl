from agents.base import BaseAgent

class DeepResearchAgent(BaseAgent):
    name = "deep_research"
    def execute(self, task):
        return f"Derin araştırma planı: soruyu parçala → çoklu kaynak → çelişki analizi → sentez. Görev: {task}"
