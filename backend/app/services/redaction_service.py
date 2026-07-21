from app.exceptions import invalid_request
from app.logger import logger
from app.services.nlp_service import NLPService

# temporary only member 3
from app.services.pseudonym_service import replace_sensitive_data
from app.mock.dumy_entities import DUMMY_ENTITIES
from app.mock.dumy_text import DUMMY_TEXT


class RedactionService:

    @staticmethod
    def redact_text(text: str):

        logger.info("Redaction request received")

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        # redacted = NLPService.redact(text)

        # temporary for member 3
        redacted = replace_sensitive_data(
            text,
            DUMMY_TEXT
            )

        return {
            "original_text": text,
            "redacted_text": redacted,
            "status": "success"
        }

    @staticmethod
    def restore_text(text: str):

        logger.info("Restore request received")

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        return {
            "restored_text": text,
            "status": "success"
        }