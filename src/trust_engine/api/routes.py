from fastapi import APIRouter
from pydantic import BaseModel

from src.trust_engine.services.trust_service import TrustService


router = APIRouter(prefix="/trust", tags=["Runtime Trust Engine"])


class TrustEvaluationRequest(BaseModel):
    retrieval_integrity: float
    governance_integrity: float
    validation_consistency: float
    authority_confidence: float
    operational_risk: float


@router.post("/evaluate")
def evaluate_trust(request: TrustEvaluationRequest):
    return TrustService.calculate_runtime_trust(
        retrieval_integrity=request.retrieval_integrity,
        governance_integrity=request.governance_integrity,
        validation_consistency=request.validation_consistency,
        authority_confidence=request.authority_confidence,
        operational_risk=request.operational_risk,
    )
