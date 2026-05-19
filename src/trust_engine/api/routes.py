from fastapi import APIRouter
from pydantic import BaseModel

from src.trust_engine.services.trust_service import TrustService
from src.governance_events.services.event_service import EventService


router = APIRouter(prefix="/trust", tags=["Runtime Trust Engine"])


class TrustEvaluationRequest(BaseModel):
    retrieval_integrity: float
    governance_integrity: float
    validation_consistency: float
    authority_confidence: float
    operational_risk: float


@router.post("/evaluate")
def evaluate_trust(request: TrustEvaluationRequest):
    trust_result = TrustService.calculate_runtime_trust(
        retrieval_integrity=request.retrieval_integrity,
        governance_integrity=request.governance_integrity,
        validation_consistency=request.validation_consistency,
        authority_confidence=request.authority_confidence,
        operational_risk=request.operational_risk,
    )

    governance_event = EventService.create_event(
        event_type="RUNTIME_TRUST_EVALUATED",
        runtime_state=trust_result.runtime_state,
        trust_score=trust_result.composite_score,
        governance_risk_level="HIGH" if trust_result.escalation_required else "LOW",
        escalation_required=trust_result.escalation_required,
        governance_actions=trust_result.governance_actions,
    )

    return {
        "trust_evaluation": trust_result,
        "governance_event": governance_event
    }
