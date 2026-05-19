from datetime import datetime
from uuid import uuid4

from src.governance_events.models.governance_event import GovernanceEvent


class EventService:

    @staticmethod
    def create_event(
        event_type: str,
        runtime_state: str,
        trust_score: float,
        governance_risk_level: str,
        escalation_required: bool,
        governance_actions: list
    ) -> GovernanceEvent:

        return GovernanceEvent(
            event_id=str(uuid4()),
            event_type=event_type,
            runtime_state=runtime_state,
            trust_score=trust_score,
            governance_risk_level=governance_risk_level,
            escalation_required=escalation_required,
            governance_actions=governance_actions,
            timestamp=datetime.utcnow()
        )
