import re

ID_PATTERNS = [

    # ==========================================
    # PATIENT IDENTIFIERS
    # ==========================================

    # Patient ID
    r"\b(?:PAT|PID)[- ]?\d{3,10}\b",

    # Medical Record Number
    r"\bMRN[- ]?\d{3,12}\b",

    # Unit Record
    r"\bUR[- ]?\d{3,12}\b",

    # Medical ID
    r"\bMED[- ]?\d{3,12}\b",

    # Patient IHS / SATUSEHAT
    r"\bP\d{11}\b",


    # ==========================================
    # INDONESIA IDENTIFIERS
    # ==========================================

    # NIK
    r"\bNIK[:\s-]*\d{16}\b",

    # KK
    r"\b(?:KK|Kartu\s+Keluarga)[:\s-]*\d{16}\b",

    # Passport
    r"\b(?:PASPOR|PASSPORT)[\s]*(?:NO|NUMBER|ID)?[:\s-]*[A-Z0-9]{6,15}\b",

    # KITAS / KITAP
    r"\b(?:KITAS|KITAP)[:\s-]*[A-Z0-9./-]{5,20}\b",


    # ==========================================
    # INSURANCE
    # ==========================================

    # Insurance ID
    r"\b(?:INS|INSURANCE)[- ]?(?:ID)?[:\s-]*[A-Z0-9]{4,20}\b",

    # Member ID
    r"\b(?:MEMBER|MEM)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9]{4,20}\b",

    # Subscriber ID
    r"\b(?:SUB|SUBSCRIBER)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9]{4,20}\b",

    # Policy Number
    r"\b(?:POL|POLICY)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9]{4,20}\b",


    # ==========================================
    # PROFESSIONAL IDENTIFIERS
    # ==========================================

    # Provider ID
    r"\b(?:PRV|PROVIDER)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9]{4,20}\b",

    # Practitioner ID
    r"\b(?:PRA|PRACTITIONER)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9]{4,20}\b",

    # STR Indonesia
    r"\b(?:STR|S\.T\.R\.)[:\s-]*[A-Z0-9./-]{6,30}\b",


    # ==========================================
    # CLINICAL IDENTIFIERS
    # ==========================================

    # Accession ID
    r"\b(?:ACC|ACCN|ACCESSION)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9-]{4,20}\b",

    # Specimen ID
    r"\b(?:SPEC|SPECIMEN)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9-]{4,20}\b",

    # Order ID
    r"\b(?:ORD|ORDER)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9-]{4,20}\b",

    # Encounter ID
    r"\b(?:ENC|ENCOUNTER)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9-]{4,20}\b",

    # Visit ID
    r"\b(?:VIS|VISIT)[- ]?(?:ID|NO|NUMBER)?[:\s-]*[A-Z0-9-]{4,20}\b",

]

def normalize_id(raw: str) -> str:
    value = raw.strip().upper()

    # Hapus label identifier di bagian awal.
    value = re.sub(
        r"^(?:"
        r"PAT|PID|MRN|UR|MED|P|"
        r"NIK|KK|KARTU\s+KELUARGA|"
        r"PASPOR|PASSPORT|"
        r"KITAS|KITAP|"
        r"INS|INSURANCE|"
        r"MEMBER|MEM|"
        r"SUBSCRIBER|SUB|"
        r"POLICY|POL|"
        r"PROVIDER|PRV|"
        r"PRACTITIONER|PRA|"
        r"STR|S\.T\.R\.|"
        r"ACCESSION|ACCN|ACC|"
        r"SPECIMEN|SPEC|"
        r"ORDER|ORD|"
        r"ENCOUNTER|ENC|"
        r"VISIT|VIS"
        r")"
        r"(?:[\s:/.-]*(?:ID|NO|NUMBER))?"
        r"[\s:/.-]*",
        "",
        value,
        flags=re.IGNORECASE
    )

    # Hilangkan spasi, titik, slash, dan dash.
    value = re.sub(r"[\s./-]+", "", value)

    return value

def calculate_id_confidence(
    raw: str,
    normalized: str,
    pattern: str
) -> float:
    score = 0.0

    # -----------------------------------------------------
    # 1. Regex berhasil melakukan matching
    # -----------------------------------------------------

    score += 0.50

    # -----------------------------------------------------
    # 2. Normalized value tersedia
    # -----------------------------------------------------

    if normalized:
        score += 0.15

    # -----------------------------------------------------
    # 3. Identifier memiliki struktur alphanumeric
    # -----------------------------------------------------

    if re.fullmatch(r"[A-Z0-9]+", normalized):
        score += 0.15

    # -----------------------------------------------------
    # 4. Panjang identifier masuk akal
    # -----------------------------------------------------

    if 4 <= len(normalized) <= 30:
        score += 0.10

    # -----------------------------------------------------
    # 5. Pattern memiliki keyword identifier
    # -----------------------------------------------------

    identifier_keywords = (
        "PAT",
        "PID",
        "MRN",
        "NIK",
        "KK",
        "PASPOR",
        "PASSPORT",
        "KITAS",
        "KITAP",
        "INS",
        "MEM",
        "SUB",
        "POL",
        "PROVIDER",
        "PRV",
        "PRA",
        "STR",
        "ACC",
        "SPEC",
        "ORD",
        "ENC",
        "VIS"
    )

    pattern_upper = pattern.upper()

    if any(
        keyword in pattern_upper
        for keyword in identifier_keywords
    ):
        score += 0.10

    return round(min(score, 1.0), 2)


def detect_id(text: str):

    entities = []

    for pattern in ID_PATTERNS:

        for match in re.finditer(
            pattern,
            text,
            flags=re.IGNORECASE
        ):

            raw = match.group()

            # ---------------------------------------------
            # NORMALIZE
            # ---------------------------------------------

            normalized = normalize_id(raw)

            # ---------------------------------------------
            # CONFIDENCE
            # ---------------------------------------------

            confidence = calculate_id_confidence(
                raw=raw,
                normalized=normalized,
                pattern=pattern
            )

            # ---------------------------------------------
            # ENTITY
            # ---------------------------------------------

            entities.append({
                "start": match.start(),
                "end": match.end(),
                "text": raw,
                "entity_type": "ID",
                "normalized": normalized,
                "confidence": confidence
            })

    # Urutkan berdasarkan posisi entity dalam text
    entities.sort(
        key=lambda entity: entity["start"]
    )

    return entities

def redact_id(text: str):
    for pattern in ID_PATTERNS:
        text = re.sub(pattern, "[ID]", text)
    return text

if __name__ == "__main__":
    print("="*50)
    print("Detected ID")
    print("="*50)

    print("="*50)
    print("Redacted")
    print("="*50)