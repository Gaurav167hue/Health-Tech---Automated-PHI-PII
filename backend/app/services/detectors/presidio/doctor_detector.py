from app.utils.normalizer import normalize_entity
from app.utils.confidence import calculate_context_confidence


DOCTOR_KEYWORDS = {
    "dr.",
    "dr",
    "doctor",
    "physician",
    "consultant",
    "dokter"
}


def classify_doctor(
    text: str,
    entities: list[dict]
) -> list[dict]:

    results = []

    for entity in entities:

        # ==========================================
        # HANYA PROSES PERSON
        # ==========================================

        if entity["entity_type"] != "PERSON":
            continue

        # ==========================================
        # AMBIL TEKS SEBELUM ENTITY
        # ==========================================

        text_before = text[
            :entity["start"]
        ].strip()

        tokens = text_before.split()

        last_token = (
            tokens[-1]
            .lower()
            .strip(".,;:!")
            if tokens
            else ""
        )

        # ==========================================
        # HARUS MEMILIKI KEYWORD DOCTOR
        # ==========================================

        if last_token not in DOCTOR_KEYWORDS:
            continue

        # ==========================================
        # VALUE
        # ==========================================

        value = text[
            entity["start"]:
            entity["end"]
        ]

        normalized = normalize_entity(
            value
        )

        # ==========================================
        # CONFIDENCE
        # ==========================================

        base_score = entity.get(
            "confidence",
            0.5
        )

        confidence = calculate_context_confidence(
            base_score,
            1.0
        )

        # ==========================================
        # RESULT
        # ==========================================

        results.append({
            "start": entity["start"],
            "end": entity["end"],
            "text": value,
            "entity_type": "DOCTOR",
            "normalized": normalized,
            "confidence": confidence
        })

    return results