class GovernanceEvaluator:

    @staticmethod
    def evaluate(
        policy_alignment: bool,
        escalation_ready: bool,
        governance_confidence: float
    ) -> float:

        score = governance_confidence

        if not policy_alignment:
            score -= 30

        if not escalation_ready:
            score -= 20

        return max(0, min(score, 100))
