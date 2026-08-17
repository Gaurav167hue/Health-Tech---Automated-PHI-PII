from app.utils.normalizer import normalize_entity
from app.utils.confidence import calculate_context_confidence


PATIENT_KEYWORDS = {
    "patient",
    "pasien"
}


DOCTOR_KEYWORDS = {
    "dr.",
    "dr",
    "doctor",
    "physician",
    "consultant",
    "dokter"
}


def classify_patient(
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
        # AMBIL KONTEKS SEBELUM ENTITY
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
        # JIKA DIDAHULUI KEYWORD DOCTOR
        # JANGAN JADIKAN PATIENT
        # ==========================================

        if last_token in DOCTOR_KEYWORDS:
            continue

        # ==========================================
        # AMBIL VALUE
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

        # Jika ada keyword patient/pasien
        context_score = 1.0 if (
            last_token in PATIENT_KEYWORDS
        ) else 0.8

        confidence = calculate_context_confidence(
            base_score,
            context_score
        )

        # ==========================================
        # RESULT
        # ==========================================

        results.append({
            "start": entity["start"],
            "end": entity["end"],
            "text": value,
            "entity_type": "PATIENT",
            "normalized": normalized,
            "confidence": confidence
        })

    return results