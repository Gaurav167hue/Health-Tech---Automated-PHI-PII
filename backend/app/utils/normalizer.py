import re

def normalize_entity(text: str) -> str:
    if not text:
        return ""

    text = text.strip()

    # Gabungkan whitespace berlebih
    text = re.sub(r"\s+", " ", text)

    return text