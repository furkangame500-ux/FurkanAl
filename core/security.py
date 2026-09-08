from core.models import Risk

class SecurityManager:
    def __init__(self):
        self.policies = {
            "web_access": "allowed",
            "file_access": "allowed",
            "screen_access": "ask",
            "app_control": "ask",
            "microphone": "ask",
            "camera": "denied",
            "phone_calls": "ask",
            "messaging": "ask",
            "purchases": "ask",
            "system_settings": "ask",
        }

    def allowed(self, action: str, risk: Risk, explicit_approval=False):
        if risk == Risk.HIGH and not explicit_approval:
            return False
        return self.policies.get(action, "ask") == "allowed"

    def list_policies(self):
        return self.policies
