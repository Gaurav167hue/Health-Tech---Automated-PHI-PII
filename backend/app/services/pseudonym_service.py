# # version split
# import re

# # regex
# from app.mock.regex.dumy_data_regex import DUMMY_DATA_REGEX
# from app.mock.regex.dumy_entities_regex import DUMMY_ENTITIES_REGEX
# from app.mock.regex.dumy_text_regex import DUMMY_TEXT_REGEX

# # nlp
# from app.mock.nlp.dumy_data_nlp import DUMY_DATA_NLP
# from app.mock.nlp.dumy_entities_nlp import DUMMY_ENTITIES_NLP
# from app.mock.nlp.dumy_text_nlp import DUMMY_TEXT_NLP

# def replace_from_entities(text, entities):
#     counters = {}
#     token_mapping = {}
#     redacted_text = text
#     for entity in entities:
#         entity_type = entity["type"]
#         entity_value = entity["text"]
#         counters.setdefault(entity_type, 0)
#         counters[entity_type] += 1
#         token = f"{entity_type}_{counters[entity_type]:03}"
#         redacted_text = redacted_text.replace(
#             entity_value,
#             token
#         )
#         token_mapping[token] = entity_value
#     return redacted_text, token_mapping

# def build_mapping(original_text, redacted_text):
#     token_mapping = {}
#     token_pattern = r"[A-Z]+_\d{3}"
#     original_words = original_text.split()
#     redacted_words = redacted_text.split()
#     for index, word in enumerate(redacted_words):
#         if re.fullmatch(token_pattern, word):
#             token_mapping[word] = original_words[index]
#     return token_mapping


# def replace_sensitive_data(text, data):
#     if isinstance(data, list):
#         return replace_from_entities(
#             text,
#             data
#         )
#     elif isinstance(data, dict):
#         redacted_text = data["type"]
#         original_text = data["text"]
#         mapping = build_mapping(
#             original_text,
#             redacted_text
#         )
#         return redacted_text, mapping
#     raise ValueError("Unsupported data")


# if __name__ == "__main__":
#     result, mapping = replace_sensitive_data(
#         # regex
#         DUMMY_DATA_REGEX,
#         DUMMY_ENTITIES_REGEX,
#         DUMMY_TEXT_REGEX,

#         # nlp
#         DUMY_DATA_NLP,
#         DUMMY_ENTITIES_NLP,
#         DUMMY_TEXT_NLP
#     )

#     print("========== ORIGINAL ==========")
#     # regex
#     print(DUMMY_DATA_REGEX)
#     print(DUMMY_ENTITIES_REGEX)
#     print(DUMMY_TEXT_REGEX)

#     # nlp
#     print(DUMY_DATA_NLP)
#     print(DUMMY_ENTITIES_NLP)
#     print(DUMMY_TEXT_NLP)

#     print("\n========== REPLACED ==========")
#     print(result)


#     print("\n========== TOKEN MAPPING ==========")
#     print(mapping)


# # version algorithm alignment
# from difflib import SequenceMatcher
# import re

# TOKEN_PATTERN = r"[A-Z]+_\d{3}"


# def replace_from_entities(text, entities):
#     counters = {}
#     token_mapping = {}
#     redacted_text = text
#     for entity in entities:
#         entity_type = entity["type"]
#         entity_value = entity["text"]
#         counters.setdefault(entity_type, 0)
#         counters[entity_type] += 1
#         token = f"{entity_type}_{counters[entity_type]:03}"
#         redacted_text = redacted_text.replace(
#             entity_value,
#             token
#         )
#         token_mapping[token] = entity_value
#     return redacted_text, token_mapping

# def build_mapping(original_text, template_text):
#     mapping = {}
#     original_words = original_text.split()
#     template_words = template_text.split()
#     matcher = SequenceMatcher(
#         None,
#         original_words,
#         template_words
#     )

#     for tag, i1, i2, j1, j2 in matcher.get_opcodes():
#         if tag != "replace":
#             continue
#         original = " ".join(
#             original_words[i1:i2]
#         )
#         template = " ".join(
#             template_words[j1:j2]
#         )
#         tokens = re.findall(
#             TOKEN_PATTERN,
#             template
#         )
#         if len(tokens) == 1:
#             mapping[tokens[0]] = original
#     return mapping


# def replace_sensitive_data(text, data):
#     if isinstance(data, list):
#         return replace_from_entities(
#             text,
#             data
#         )
#     if isinstance(data, dict):
#         original_text = data["text"]
#         redacted_text = data["type"]
#         mapping = build_mapping(
#             original_text,
#             redacted_text
#         )
#         return redacted_text, mapping

#     raise ValueError(
#         "Unsupported data"
#     )

# # version Anchor Alignment
# import re

# TOKEN_PATTERN = r"[A-Z]+_\d{3}"


# # =====================================================
# # Helper
# # =====================================================

# def is_token(word):
#     return re.fullmatch(TOKEN_PATTERN, word) is not None


# # =====================================================
# # MODE 1
# # Entity List
# # (dipakai nanti ketika Regex / NLP selesai)
# # =====================================================

# def replace_from_entities(text, entities):
#     counters = {}
#     token_mapping = {}
#     redacted_text = text
#     for entity in entities:
#         entity_type = entity["type"]
#         entity_value = entity["text"]
#         counters.setdefault(entity_type, 0)
#         counters[entity_type] += 1
#         token = f"{entity_type}_{counters[entity_type]:03}"
#         redacted_text = redacted_text.replace(
#             entity_value,
#             token
#         )
#         token_mapping[token] = entity_value
#     return redacted_text, token_mapping


# # =====================================================
# # MODE 2
# # Anchor Alignment
# # (dipakai selama masih dummy text + type)
# # =====================================================

# def build_mapping(original_text, template_text):
#     mapping = {}
#     original = original_text.split()
#     template = template_text.split()
#     for index, word in enumerate(template):
#         if not is_token(word):
#             continue
#         token = word
#         left_anchor = None
#         right_anchor = None

#         # -------------------------------
#         # Cari anchor kiri
#         # -------------------------------
#         for i in range(index - 1, -1, -1):
#             if not is_token(template[i]):
#                 left_anchor = template[i]
#                 break

#         # -------------------------------
#         # Cari anchor kanan
#         # -------------------------------
#         for i in range(index + 1, len(template)):
#             if not is_token(template[i]):
#                 right_anchor = template[i]
#                 break

#         # -------------------------------
#         # Cari posisi anchor kiri
#         # -------------------------------
#         start = 0
#         if left_anchor:
#             for i, w in enumerate(original):
#                 if w == left_anchor:
#                     start = i + 1

#         # -------------------------------
#         # Cari posisi anchor kanan
#         # -------------------------------
#         end = len(original)
#         if right_anchor:
#             for i in range(start, len(original)):
#                 if original[i] == right_anchor:
#                     end = i
#                     break

#         entity = " ".join(
#             original[start:end]
#         )
#         mapping[token] = entity

#     return mapping

# def generate_redacted_template(template):
#     counters = {}
#     words = template.split()
#     result = []
#     for word in words:
#         if re.fullmatch(r"[A-Z]+", word):
#             counters.setdefault(word, 0)
#             counters[word] += 1
#             result.append(
#                 f"{word}_{counters[word]:03}"
#             )
#         else:
#             result.append(word)
#     return " ".join(result)


# def replace_sensitive_data(text, data):
#     if isinstance(data, list):
#         return replace_from_entities(text, data)
#     if isinstance(data, dict):
#         original = data["text"]

#         # template mentah
#         template = data["type"]

#         # kasih counter
#         redacted = generate_redacted_template(template)

#         # baru alignment
#         mapping = build_mapping(
#             original,
#             redacted
#         )

#         return redacted, mapping

# Version Cursor + Anchor Alignment
# import re
# TOKEN_PATTERN = r"[A-Z]+_\d{3}"

# # ==========================================
# # Helper
# # ==========================================
# def is_token(word):
#     return re.fullmatch(TOKEN_PATTERN, word) is not None

# # ==========================================
# # Mode 1
# # Entity List
# # ==========================================
# def replace_from_entities(text, entities):
#     counters = {}
#     mapping = {}
#     redacted = text
#     for entity in entities:
#         entity_type = entity["type"]
#         entity_text = entity["text"]
#         counters.setdefault(entity_type, 0)
#         counters[entity_type] += 1
#         token = f"{entity_type}_{counters[entity_type]:03}"
#         redacted = redacted.replace(
#             entity_text,
#             token
#         )
#         mapping[token] = entity_text
#     return redacted, mapping

# # ==========================================
# # Generate Counter
# # ==========================================
# def generate_redacted_template(template):
#     counters = {}
#     result = []
#     for word in template.split():
#         if re.fullmatch(r"[A-Z]+", word):
#             counters.setdefault(word, 0)
#             counters[word] += 1
#             result.append(
#                 f"{word}_{counters[word]:03}"
#             )
#         else:
#             result.append(word)
#     return " ".join(result)

# # ==========================================
# # Version 4
# # Anchor + Cursor Alignment
# # ==========================================
# def build_mapping(original_text, template_text):
#     mapping = {}
#     original = original_text.split()
#     template = template_text.split()
#     cursor = 0
#     for index, word in enumerate(template):
#         if not is_token(word):
#             continue
#         token = word
#         left_anchor = None
#         right_anchor = None

#         # -----------------------------
#         # Anchor kiri
#         # -----------------------------
#         for i in range(index - 1, -1, -1):
#             if not is_token(template[i]):
#                 left_anchor = template[i]
#                 break

#         # -----------------------------
#         # Anchor kanan
#         # -----------------------------
#         for i in range(index + 1, len(template)):
#             if not is_token(template[i]):
#                 right_anchor = template[i]
#                 break

#         # -----------------------------
#         # Cari start
#         # -----------------------------
#         start = cursor
#         if left_anchor:
#             for i in range(cursor, len(original)):
#                 if original[i] == left_anchor:
#                     start = i + 1
#                     break

#         # -----------------------------
#         # Cari end
#         # -----------------------------
#         end = len(original)
#         if right_anchor:
#             for i in range(start, len(original)):
#                 if original[i] == right_anchor:
#                     end = i
#                     break
#         entity = " ".join(
#             original[start:end]
#         )
#         mapping[token] = entity

#         # ===================================
#         # Cursor maju
#         # ===================================
#         cursor = end
#     return mapping

# # ==========================================
# # Wrapper
# # ==========================================

# def replace_sensitive_data(text, data):
#     # Entity Mode
#     if isinstance(data, list):
#         return replace_from_entities(
#             text,
#             data
#         )
#     # Dummy Template Mode
#     if isinstance(data, dict):
#         original = data["text"]
#         template = data["type"]
#         redacted = generate_redacted_template(
#             template
#         )
#         mapping = build_mapping(
#             original,
#             redacted
#         )
#         return (
#             redacted,
#             mapping
#         )
#     raise ValueError(
#         "Unsupported data format"
#     )

# Version Progressive Anchor Matching
import re
from app.database.redis_client import redis_client
from app.repositories.token_repositories import TokenRepository

TOKEN_PATTERN = r"\b[A-Z]+_\d{3}\b"
token_repository = TokenRepository()


# ==========================================
# Helper
# ==========================================

def is_token(word):
    return re.fullmatch(TOKEN_PATTERN, word) is not None


# ==========================================
# MODE 1
# Entity List
# ==========================================
def replace_from_entities(text, entities):
    counters = {}
    mapping = {}
    redacted = text
    for entity in entities:
        entity_type = entity["type"]
        entity_text = entity["text"]
        counters.setdefault(entity_type, 0)
        counters[entity_type] += 1
        token = f"{entity_type}_{counters[entity_type]:03}"
        redacted = redacted.replace(
            entity_text,
            token,
            1
        )
        mapping[token] = entity_text
    return redacted, mapping


# ==========================================
# Counter Generator
# ==========================================
def generate_redacted_template(template):
    counters = {}
    result = []
    for word in template.split():
        if re.fullmatch(r"[A-Z]+", word):
            counters.setdefault(word, 0)
            counters[word] += 1
            result.append(
                f"{word}_{counters[word]:03}"
            )
        else:
            result.append(word)
    return " ".join(result)


# ==========================================
# Version 5
# Sequential Window Matching
# ==========================================
def build_mapping(original_text, template_text):
    mapping = {}
    original = original_text.split()
    template = template_text.split()
    original_cursor = 0
    for index, word in enumerate(template):
        if not is_token(word):
            continue
        token = word

        # ------------------------
        # cari anchor kiri
        # ------------------------
        left_anchor = None
        for i in range(index - 1, -1, -1):
            if not is_token(template[i]):
                left_anchor = template[i]
                break

        # ------------------------
        # cari anchor kanan
        # ------------------------
        right_anchor = None
        for i in range(index + 1, len(template)):
            if not is_token(template[i]):
                right_anchor = template[i]
                break

        # ------------------------
        # start
        # ------------------------
        start = original_cursor
        if left_anchor:
            for i in range(original_cursor, len(original)):
                if original[i] == left_anchor:
                    start = i + 1
                    break

        # ------------------------
        # end
        # ------------------------
        end = len(original)
        if right_anchor:
            for i in range(start, len(original)):
                if original[i] == right_anchor:
                    end = i
                    break
        entity = " ".join(
            original[start:end]
        )
        mapping[token] = entity
        original_cursor = end
    return mapping

# ==========================================
# Restore
# Regex Token Matching
# ==========================================
def restore_sensitive_data(redacted_text):
    def replace_token(match):
        token = match.group()
        value = token_repository.get(token)
        if value is not None:
            return value
        return token
    restored_text = re.sub(
        TOKEN_PATTERN,
        replace_token,
        redacted_text
    )
    return restored_text

# ==========================================
# Wrapper
# ==========================================
def replace_sensitive_data(text, data):
    if isinstance(data, list):
        redacted, mapping = replace_from_entities(
            text,
            data
        )

        token_repository.save_many(
            mapping,
        )

        return (
            redacted,
            mapping
        )
    if isinstance(data, dict):
        original = data["text"]
        template = data["type"]

        redacted = generate_redacted_template(
            template
        )

        mapping = build_mapping(
            original,
            redacted
        )

        token_repository.save_many(
            mapping,
        )

        return (
            redacted,
            mapping
        )
    raise ValueError(
        "Unsupported data format"
    )

# ==========================================
# Restore
# Regex Token Matching
# ==========================================
def restore_sensitive_data(redacted_text):
    tokens = re.findall(
        TOKEN_PATTERN,
        redacted_text
    )
    token_mapping = token_repository.get_many(
        tokens
    )
    restored_text = redacted_text
    for token, value in token_mapping.items():
        restored_text = restored_text.replace(
            token,
            value
        )
    return restored_text, token_mapping