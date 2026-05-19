from src.trust_engine.models.trust_score import TrustScore


class TrustService:

    @staticmethod
    def calculate_runtime_trust(
        retrieval_integrity: float,
        governance_integrity: float,
        validation_consistency: float,
        authority_confidence: float,
        operational_risk: float
    ) -> TrustScore:

        composite_score = (
            retrieval_integrity
            + governance_integrity
            + validation_consistency
            + authority_confidence
        ) / 4

        composite_score = composite_score - operational_risk

        if composite_score >= 85:
            runtime_state = "TRUSTED"
            escalation_required = False
            governance_actions = ["allow_execution"]

        elif composite_score >= 70:
            runtime_state = "MONITORED"
            escalation_required = False
            governance_actions = [
                "enable_observability",
                "track_runtime_state"
            ]

        elif composite_score >= 50:
            runtime_state = "RESTRICTED"
            escalation_required = True
            governance_actions = [
                "restrict_execution",
                "require_manual_review"
            ]

        elif composite_score >= 30:
            runtime_state = "ESCALATED"
            escalation_required = True
            governance_actions = [
                "pause_execution",
                "trigger_supervisory_review"
            ]

        else:
            runtime_state = "BLOCKED"
            escalation_required = True
            governance_actions = [
                "deny_execution",
                "activate_governance_lockdown"
            ]

        return TrustScore(
            retrieval_integrity=retrieval_integrity,
            governance_integrity=governance_integrity,
            validation_consistency=validation_consistency,
            authority_confidence=authority_confidence,
            operational_risk=operational_risk,
            composite_score=round(composite_score, 2),
            runtime_state=runtime_state,
            escalation_required=escalation_required,
            governance_actions=governance_actions
        )
