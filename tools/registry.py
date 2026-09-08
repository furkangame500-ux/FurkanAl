class CapabilityRegistry:
    def __init__(self):
        self.capabilities = {}

    def register(self, name, handler, permissions=None, risk="low"):
        self.capabilities[name] = {
            "handler": handler,
            "permissions": permissions or [],
            "risk": risk,
        }

    def discover(self):
        return {
            name: {k: v for k, v in spec.items() if k != "handler"}
            for name, spec in self.capabilities.items()
        }
