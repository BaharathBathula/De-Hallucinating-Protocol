class AuthorityEvaluator:

    @staticmethod
    def evaluate(
        trusted_source: bool,
        regulatory_verified: bool,
        authority_confidence: float
    ) -> float:

        score = authority_confidence

        if not trusted_source:
            score -= 35

        if not regulatory_verified:
            score -= 15

        return max(0, min(score, 100))
