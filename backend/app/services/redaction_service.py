from app.exceptions import invalid_request
from app.logger import logger


class RedactionService:

    @staticmethod
    def redact_text(text: str):

        logger.info("Redaction request received")

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        return {
            "original_text": text,
            "redacted_text": text,
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