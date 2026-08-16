from presidio_analyzer import RecognizerResult

from app.utils.normalizer import normalize_entity


def detect_person(
    text: str,
    entities: list[RecognizerResult]
) -> list[dict]:

    results = []

    for entity in entities:

        if entity.entity_type != "PERSON":
            continue

        value = normalize_entity(
            text[entity.start:entity.end]
        )

        results.append({
            "start": entity.start,
            "end": entity.end,
            "text": value,
            "entity_type": "PERSON",
            "normalized": value,
            "confidence": round(
                max(0.0, min(entity.score, 1.0)),
                2
            )
        })

    return results