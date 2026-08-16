import re
from datetime import datetime


DATE_PATTERN = (
    r"\b(?:"
    r"\d{2}[/-]\d{2}[/-]\d{4}"                 # 20/07/2026 atau 20-07-2026
    r"|"
    r"\d{4}-\d{2}-\d{2}"                       # 2026-07-20
    r"|"
    r"\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|"
    r"January|February|March|April|May|June|July|August|"
    r"September|October|November|December)\s\d{4}"
    r")\b"
)


# =========================================================
# DATE NORMALIZATION
# =========================================================

def normalize_date(raw: str) -> str | None:
    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d",
        "%d %b %Y",
        "%d %B %Y",
    ]

    raw = raw.strip()

    for date_format in formats:
        try:
            date = datetime.strptime(raw, date_format)
            return date.strftime("%Y-%m-%d")
        except ValueError:
            continue

    return None


# =========================================================
# DATE CONFIDENCE
# =========================================================

def calculate_date_confidence(
    raw: str,
    normalized: str | None
) -> float:

    # Jika tanggal gagal dinormalisasi,
    # berarti tanggal tidak valid.
    if normalized is None:
        return 0.0

    score = 0.0

    # -----------------------------------------------------
    # 1. Tanggal berhasil diparse
    # -----------------------------------------------------
    score += 0.60

    # -----------------------------------------------------
    # 2. Format tanggal dikenali dengan jelas
    # -----------------------------------------------------
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", raw):
        score += 0.15

    elif re.fullmatch(r"\d{2}-\d{2}-\d{4}", raw):
        score += 0.15

    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        score += 0.20

    elif re.fullmatch(
        r"\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|"
        r"January|February|March|April|May|June|July|August|"
        r"September|October|November|December)\s\d{4}",
        raw,
        re.IGNORECASE
    ):
        score += 0.20

    # -----------------------------------------------------
    # 3. Tahun berada dalam range yang masuk akal
    # -----------------------------------------------------
    year = int(normalized[:4])

    if 1900 <= year <= 2100:
        score += 0.20

    return round(min(score, 1.0), 2)


# =========================================================
# DATE DETECTION
# =========================================================

def detect_date(text: str):
    entities = []

    for match in re.finditer(DATE_PATTERN, text):

        raw = match.group()

        # Normalisasi
        normalized = normalize_date(raw)

        # Jangan masukkan tanggal yang tidak valid
        if normalized is None:
            continue

        # Hitung confidence
        confidence = calculate_date_confidence(
            raw,
            normalized
        )

        entities.append({
            "start": match.start(),
            "end": match.end(),
            "text": raw,
            "entity_type": "DATE",
            "normalized": normalized,
            "confidence": confidence
        })

    return entities


# =========================================================
# REDACTION
# =========================================================

def redact_date(text: str):
    return re.sub(DATE_PATTERN, "[DATE]", text)


# =========================================================
# MANUAL TEST
# =========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Detected Date")
    print("=" * 50)

    print()

    print("=" * 50)
    print("Redacted Text")
    print("=" * 50)
