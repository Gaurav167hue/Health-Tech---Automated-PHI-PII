import re

from presidio_analyzer import RecognizerResult

from app.utils.normalizer import normalize_entity
from app.utils.confidence import calculate_context_confidence


ADDRESS_KEYWORDS = {
    "street",
    "road",
    "avenue",
    "district",
    "city",
    "jalan",
    "jl",
    "kelurahan",
    "kecamatan",
    "kota",
    "rt",
    "rw",
}


def _has_address_context(context: str) -> bool:
    words = context.lower().split()

    return any(
        keyword in words
        for keyword in ADDRESS_KEYWORDS
    )


def detect_address(
    text: str,
    entities: list[RecognizerResult],
) -> list[dict]:

    results = []

    detected_spans = set()

    # ==========================================
    # PRESIDIO LOCATION
    # ==========================================

    for entity in entities:

        if entity.entity_type != "LOCATION":
            continue

        value = normalize_entity(
            text[entity.start:entity.end]
        )

        before = text[
            max(0, entity.start - 40):
            entity.start
        ]

        after = text[
            entity.end:
            min(len(text), entity.end + 40)
        ]

        context = f"{before} {value} {after}"

        if not _has_address_context(context):
            continue

        confidence = calculate_context_confidence(
            entity.score,
            1.0
        )

        results.append({
            "start": entity.start,
            "end": entity.end,
            "text": value,
            "entity_type": "ADDRESS",
            "normalized": value,
            "confidence": confidence,
        })

        detected_spans.add(
            (entity.start, entity.end)
        )

    # ==========================================
    # REGEX JALAN
    # ==========================================

    pattern_jalan = re.compile(
        r"\b(?:Jalan|Jl\.?|Jln)\s+"
        r"[A-Z][\w\s]*?"
        r"(?:\s+No\.?\s*\d+)?\b",
        re.IGNORECASE
    )

    for match in pattern_jalan.finditer(text):

        span = (match.start(), match.end())

        if span in detected_spans:
            continue

        value = normalize_entity(
            match.group()
        )

        results.append({
            "start": match.start(),
            "end": match.end(),
            "text": value,
            "entity_type": "ADDRESS",
            "normalized": value,
            "confidence": 0.85,
        })

        detected_spans.add(span)

    # ==========================================
    # REGEX RT/RW
    # ==========================================

    pattern_rt_rw = re.compile(
        r"\bRT\.?\s*\d{1,3}"
        r"\s*/\s*"
        r"RW\.?\s*\d{1,3}\b",
        re.IGNORECASE
    )

    for match in pattern_rt_rw.finditer(text):

        span = (match.start(), match.end())

        if span in detected_spans:
            continue

        value = normalize_entity(
            match.group()
        )

        results.append({
            "start": match.start(),
            "end": match.end(),
            "text": value,
            "entity_type": "ADDRESS",
            "normalized": value,
            "confidence": 0.85,
        })

        detected_spans.add(span)

    return results