from app.exceptions import invalid_request
from app.logger import logger
from app.services.nlp_service import NLPService
from app.services.detection_service import DetectionService


class RedactionService:

    @staticmethod
    def redact_text(text: str):

        logger.info("Redaction request received")

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        # Member 1 
        redacted = NLPService.redact(text)

        # Member 2
        entities = DetectionService.detect(text)

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