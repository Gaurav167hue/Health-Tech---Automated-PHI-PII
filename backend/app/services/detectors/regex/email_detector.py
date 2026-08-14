import re

EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

def normalize_email(raw: str) -> str:
    return raw.strip().lower()

def calculate_email_confidence(email: str) -> float:
    score = 0.50

    # --------------------------------
    # 1. Struktur dasar email
    # --------------------------------
    if "@" in email:
        score += 0.15

    # --------------------------------
    # 2. Local part sebelum @
    # --------------------------------
    local, _, domain = email.partition("@")

    if local:
        score += 0.10

    # --------------------------------
    # 3. Domain
    # --------------------------------
    if domain:
        score += 0.05

    # --------------------------------
    # 4. Domain memiliki TLD
    # contoh: gmail.com
    # --------------------------------
    if re.search(r"\.[A-Za-z]{2,}$", domain):
        score += 0.10

    # --------------------------------
    # 5. Tidak mengandung whitespace
    # --------------------------------
    if not re.search(r"\s", email):
        score += 0.05

    # --------------------------------
    # 6. Tidak memiliki @ berlebihan
    # --------------------------------
    if email.count("@") == 1:
        score += 0.05

    # Batasi 0.0 - 1.0
    return round(min(max(score, 0.0), 1.0), 2)

def detect_email(text: str):
    entities = []
    for match in re.finditer(EMAIL_PATTERN, text):
        raw = match.group()
        normalized = normalize_email(raw)
        confidence = calculate_email_confidence(raw)

        entities.append({
            "start": match.start(),
            "end": match.end(),
            "text": match.group(),
            "entity_type": "EMAIL",
            "normalized": normalized,
            "confidence": confidence
        })
    return entities


def redact_email(text: str):
    return re.sub(EMAIL_PATTERN, "[EMAIL]", text)

if __name__ == "__main__":

    print("=" * 50)
    print("Detected Email")
    print("=" * 50)

    print("\n")

    print("=" * 50)
    print("Redacted Text")
    print("=" * 50)
