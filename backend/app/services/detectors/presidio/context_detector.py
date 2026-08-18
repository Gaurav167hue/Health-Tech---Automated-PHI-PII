import re

from app.utils.normalizer import normalize_entity


MEDICAL_CONTEXT = {
    "disease",
    "syndrome",
    "disorder",
    "infection",
    "cancer",
    "diabetes",
    "hypertension",
    "parkinson",
    "alzheimer"
    "tuberculosis",
    "stroke",
    "asthma",
    "pneumonia",
    "migraine",
    "arthritis",
    "heart disease",
    "kidney disease",
    "liver disease",
}


def calculate_context_confidence(
    value: str,
    context: str,
) -> float:

    value_lower = value.lower()

    # Exact medical term
    if value_lower in MEDICAL_CONTEXT:
        return 0.95

    # Medical term berada dalam context
    if any(
        keyword in context.lower()
        for keyword in MEDICAL_CONTEXT
    ):
        return 0.85

    return 0.70


def detect_context(text: str) -> list[dict]:

    results = []

    for keyword in MEDICAL_CONTEXT:

        pattern = re.compile(
            rf"\b{re.escape(keyword)}\b",
            re.IGNORECASE
        )

        for match in pattern.finditer(text):

            value = normalize_entity(
                match.group()
            )

            confidence = calculate_context_confidence(
                value,
                text
            )

            results.append({
                "start": match.start(),
                "end": match.end(),
                "text": value,
                "entity_type": "CONTEXT",
                "normalized": value.lower(),
                "confidence": confidence,
            })

    return results

    # "disease",
    # "syndrome",
    # "disorder",
    # "infection",
    # "cancer",
    # "diabetes",
    # "hypertension",
    # "parkinson",
    # "alzheimer"
    # "tuberculosis",
    # "stroke",
    # "asthma",
    # "pneumonia",
    # "migraine",
    # "arthritis",
    # "heart disease",
    # "kidney disease",
    # "liver disease",