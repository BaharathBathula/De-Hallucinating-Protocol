class RetrievalEvaluator:

    @staticmethod
    def evaluate(source_verified: bool, provenance_valid: bool, retrieval_confidence: float) -> float:
        score = retrieval_confidence

        if not source_verified:
            score -= 25

        if not provenance_valid:
            score -= 25

        return max(0, min(score, 100))
