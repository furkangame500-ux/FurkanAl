from agents.research.agent import ResearchAgent
from agents.coding.agent import CodingAgent
from agents.media.agent import MediaAgent
from agents.personalization.agent import PersonalizationAgent
from agents.emotion.agent import EmotionAgent
from agents.deep_research.agent import DeepResearchAgent
from agents.self_improvement.agent import SelfImprovementAgent

class AgentManager:
    def __init__(self):
        self.agents = {
            "research": ResearchAgent(),
            "coding": CodingAgent(),
            "media": MediaAgent(),
            "personalization": PersonalizationAgent(),
            "emotion": EmotionAgent(),
            "deep_research": DeepResearchAgent(),
            "self_improvement": SelfImprovementAgent(),
        }

    def list_agents(self):
        return list(self.agents.keys())

    def run(self, name, task, autonomy_level):
        return self.agents[name].run(task, autonomy_level)
