from pydantic import BaseModel
from typing import List


class TrustScore(BaseModel):
    retrieval_integrity: float
    governance_integrity: float
    validation_consistency: float
    authority_confidence: float
    operational_risk: float

    composite_score: float
    runtime_state: str
    escalation_required: bool

    governance_actions: List[str]
