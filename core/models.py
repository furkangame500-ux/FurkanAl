from enum import Enum
from typing import Any
from pydantic import BaseModel, Field

class Risk(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskRequest(BaseModel):
    message: str
    autonomy_level: int = Field(default=1, ge=0, le=4)

class AgentResult(BaseModel):
    agent: str
    success: bool
    output: str
    risk: Risk = Risk.LOW
    metadata: dict[str, Any] = {}

class MemoryRecord(BaseModel):
    content: str
    category: str
    source: str = "system"
    confidence: float = Field(default=0.5, ge=0, le=1)
    timestamp: str
