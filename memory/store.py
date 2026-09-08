from datetime import datetime, timezone

class MemoryStore:
    def __init__(self):
        self.records = []

    def add(self, content, category, source="system", confidence=0.5):
        self.records.append({
            "content": content,
            "category": category,
            "source": source,
            "confidence": confidence,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

    def list_recent(self):
        return self.records[-50:]
