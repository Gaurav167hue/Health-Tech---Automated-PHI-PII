from app.mock.dumy_text import DUMMY_TEXT
from app.mock.dumy_entities import DUMMY_ENTITIES

def replace_sensitive_data(text, entities):
    # Counter untuk setiap jenis entity
    counters = {}

    # Salinan text
    replaced_text = text

    # Loop seluruh entity
    for entity in entities:
        entity_type = entity["type"]
        entity_value = entity["text"]

        # Jika tipe belum ada maka mulai dari 1
        if entity_type not in counters:
            counters[entity_type] = 1

        # Membuat token
        token = f"{entity_type}_{counters[entity_type]:03}"

        # Replace text
        replaced_text = replaced_text.replace(
            entity_value,
            token
        )

        # Counter naik
        counters[entity_type] += 1
    return replaced_text


if __name__ == "__main__":
    result = replace_sensitive_data(
        DUMMY_TEXT,
        DUMMY_ENTITIES
    )

    print("========== ORIGINAL ==========")
    print(DUMMY_TEXT)

    print("\n========== REPLACED ==========")
    print(result)