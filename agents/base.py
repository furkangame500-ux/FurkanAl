class BaseAgent:
    name = "base"

    def run(self, task, autonomy_level=1):
        return {
            "agent": self.name,
            "success": True,
            "output": self.execute(task),
            "autonomy_level": autonomy_level,
        }

    def execute(self, task):
        raise NotImplementedError
