from app.exceptions import invalid_request
from app.logger import logger
from app.services.detection_service import DetectionService

from app.services.pseudonym_service import (
    replace_sensitive_data,
    restore_sensitive_data
)


class RedactionService:

    @staticmethod
    def redact_text(text: str):

        logger.info("Redaction request received")

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        # Member 2 + Member 3
        entities = DetectionService.detect(text)

        # Member 4 - Pseudonymization + Token Mapping
        redacted_text, token_mapping = replace_sensitive_data(
            text,
            entities
        )

        return {
            "original_text": text,
            "redacted_text": redacted_text,
            "token_mapping": token_mapping,
            "status": "success"
        }
