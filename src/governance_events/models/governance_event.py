from pydantic import BaseModel
from typing import List
from datetime import datetime


class GovernanceEvent(BaseModel):
    event_id: str
    event_type: str

    runtime_state: str
    trust_score: float
    governance_risk_level: str

    escalation_required: bool

    governance_actions: List[str]

    timestamp: datetime
