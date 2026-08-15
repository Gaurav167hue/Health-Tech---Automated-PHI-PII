import re

PHONE_PATTERN = re.compile(
    r"""
    (?<![\dA-Za-z])

    (?:
        \+62[\s.-]?8\d{2,4}(?:[\s.-]?\d{2,4}){1,3}

        0062[\s.-]?8\d{2,4}(?:[\s.-]?\d{2,4}){1,3}

        |

        62[\s.-]?8\d{2,4}(?:[\s.-]?\d{2,4}){1,3}

        |

        0(?:\d{2,4})?(?:[\s.-]?\d{3,4}){2,3}

        |


        \+\d{1,3}[\s.-]?\d{2,4}(?:[\s.-]?\d{2,4}){1,3}

        |

        00\d{1,3}[\s.-]?\d{2,4}(?:[\s.-]?\d{2,4}){1,3}
    )

    (?![\dA-Za-z])
    """,
    re.VERBOSE,
)

ID_CONTEXT_PATTERN = re.compile(
    r"""
    (?:
        PAT
        |PID
        |MRN
        |UR
        |MED
        |NIK
        |KK
        |ID
        |IHS
        |PASSPORT
        |PASPOR
        |KITAS
        |KITAP
        |INS
        |INSURANCE
        |MEMBER
        |MEM
        |SUB
        |SUBSCRIBER
        |POL
        |POLICY
        |PRV
        |PROVIDER
        |PRA
        |PRACTITIONER
        |STR
        |ACC
        |ACCN
        |ACCESSION
        |SPEC
        |SPECIMEN
        |ORD
        |ORDER
        |ENC
        |ENCOUNTER
        |VIS
        |VISIT
    )
    [\s:_-]*
    $
    """,
    re.IGNORECASE | re.VERBOSE,
)


# ============================================================
# HELPER
# ============================================================

def extract_digits(value: str) -> str:
    """
    Mengambil hanya digit dari string.
    """
    return re.sub(r"\D", "", value)


def is_id_context(text: str, start: int) -> bool:
    """
    Mengecek apakah kandidat PHONE sebenarnya berada setelah
    label ID seperti PAT, MRN, NIK, dll.
    """

    # Ambil sekitar 20 karakter sebelum kandidat.
    prefix = text[max(0, start - 20):start]

    return bool(ID_CONTEXT_PATTERN.search(prefix))


def is_valid_phone_length(raw: str) -> bool:
    """
    Validasi jumlah digit nomor telepon.

    Mayoritas nomor telepon berada pada range 8-15 digit.
    """

    digits = extract_digits(raw)

    return 8 <= len(digits) <= 15


# ============================================================
# NORMALIZATION
# ============================================================

def normalize_phone(raw: str) -> str:
    raw = raw.strip()

    # Hapus separator.
    value = re.sub(r"[\s().-]", "", raw)

    # 00xxxxxxxx → +xxxxxxxx
    if value.startswith("00"):
        value = "+" + value[2:]

    if value.startswith("0"):
        value = "+62" + value[1:]

    elif value.startswith("62"):
        value = "+" + value

    elif value.startswith("+"):
        pass

    else:
        value = "+" + value

    return value


# ============================================================
# CONFIDENCE
# ============================================================

def calculate_phone_confidence(raw: str, normalized: str) -> float:
    score = 0.0

    raw_clean = raw.strip()
    digits = extract_digits(raw_clean)

    # --------------------------------------------------------
    # 1. Panjang nomor
    # --------------------------------------------------------

    if 10 <= len(digits) <= 13:
        score += 0.35

    elif 8 <= len(digits) <= 15:
        score += 0.25

    # --------------------------------------------------------
    # 2. Prefix Indonesia
    # --------------------------------------------------------

    if normalized.startswith("+62"):
        score += 0.30

    # --------------------------------------------------------
    # 3. Prefix international
    # --------------------------------------------------------

    elif raw_clean.startswith(("+", "00")):
        score += 0.25

    # --------------------------------------------------------
    # 4. Format lokal Indonesia
    # --------------------------------------------------------

    elif raw_clean.startswith("0"):
        score += 0.25

    # --------------------------------------------------------
    # 5. Separator telepon valid
    # --------------------------------------------------------

    if re.fullmatch(r"[\d\s().+\-]+", raw_clean):
        score += 0.15

    # --------------------------------------------------------
    # 6. Tidak mengandung huruf
    # --------------------------------------------------------

    if not re.search(r"[A-Za-z]", raw_clean):
        score += 0.10

    return round(min(score, 1.0), 2)


# ============================================================
# DETECTION
# ============================================================

def detect_phone(text: str):
    results = []

    for match in PHONE_PATTERN.finditer(text):

        raw = match.group().strip()

        start = match.start()
        end = match.end()

        # ----------------------------------------------------
        # VALIDATION 1
        # ----------------------------------------------------

        if not is_valid_phone_length(raw):
            continue

        # ----------------------------------------------------
        # VALIDATION 2
        #
        # Cegah collision dengan ID.
        # ----------------------------------------------------

        if is_id_context(text, start):
            continue

        # ----------------------------------------------------
        # NORMALIZATION
        # ----------------------------------------------------

        normalized = normalize_phone(raw)

        # ----------------------------------------------------
        # CONFIDENCE
        # ----------------------------------------------------

        confidence = calculate_phone_confidence(
            raw,
            normalized
        )

        # ----------------------------------------------------
        # MINIMUM CONFIDENCE
        # ----------------------------------------------------

        if confidence < 0.50:
            continue

        results.append(
            {
                "start": start,
                "end": end,
                "text": raw,
                "entity_type": "PHONE",
                "normalized": normalized,
                "confidence": confidence,
            }
        )

    return results


# ============================================================
# REDACTION
# ============================================================

def redact_phone(text: str):
    entities = detect_phone(text)

    # Reverse order supaya posisi string tidak berubah
    # ketika melakukan replacement.
    for entity in reversed(entities):

        start = entity["start"]
        end = entity["end"]

        text = (
            text[:start]
            + "[PHONE]"
            + text[end:]
        )

    return text


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PHONE DETECTION")
    print("=" * 60)

    print("\n")
    print("=" * 60)
    print("REDACTED TEXT")
    print("=" * 60)
