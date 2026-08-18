from app.exceptions import invalid_request
from app.logger import logger
from app.services.nlp_service import NLPService
from app.services.detection_service import DetectionService

# temporary only member 3
from app.services.pseudonym_service import (
    replace_sensitive_data, 
    restore_sensitive_data
)

# store
# regex
from app.mock.store.regex.dumy_data_regex import DUMMY_DATA_REGEX
from app.mock.store.regex.dumy_entities_regex import DUMMY_ENTITIES_REGEX
from app.mock.store.regex.dumy_text_regex import DUMMY_TEXT_REGEX

# nlp
from app.mock.store.nlp.dumy_data_nlp import DUMY_DATA_NLP
from app.mock.store.nlp.dumy_entities_nlp import DUMMY_ENTITIES_NLP
from app.mock.store.nlp.dumy_text_nlp import DUMMY_TEXT_NLP

# restore
from app.mock.restore.nlp.dumy_text_nlp import DUMMY_TEXT_NLP_RESTORE
from app.mock.restore.regex.dumy_text_regex import DUMMY_TEXT_REGEX_RESTORE

class RedactionService:

    @staticmethod
    def redact_text(text: str):

        logger.info("Redaction request received")

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        # from member 1
        # redacted = NLPService.redact(text)

        # temporary for member 3
        redacted_text, token_mapping= replace_sensitive_data(
            text,

            # if member 2 done replace here

            # only use dumydata for member 3
            
            # regex
            # DUMMY_DATA_REGEX
            # DUMMY_ENTITIES_REGEX
            # DUMMY_TEXT_REGEX

            # nlp
            # DUMY_DATA_NLP
            # DUMMY_ENTITIES_NLP
            DUMMY_TEXT_NLP
            )
        # Member 1 
        redacted = NLPService.redact(text)

        # Member 2
        entities = DetectionService.detect(text)

        return {
            "original_text": text,
            "redacted_text": redacted_text,
            "token_mapping": token_mapping,
            "status": "success"
        }

    @staticmethod
    def restore_text(text: str):

        logger.info("Restore request received")

        if not text.strip():
            invalid_request(
                "Input text cannot be empty."
            )

        restored_text, token_mapping = restore_sensitive_data(
            text,
            # DUMMY_TEXT_NLP_RESTORE
            # DUMMY_TEXT_REGEX_RESTORE
        )

        return {
            "token_mapping": token_mapping,
            "restored_text": restored_text,
            "status": "success"
        }