def calculate_context_confidence(
    base_score: float,
    context_score: float = 0.0,
) -> float:
    base_score = max(0.0, min(base_score, 1.0))
    context_score = max(0.0, min(context_score, 1.0))

    # 80% berasal dari analyzer
    # 20% berasal dari context
    confidence = (
        base_score * 0.8
        + context_score * 0.2
    )

    return round(min(confidence, 1.0), 2)