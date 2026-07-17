class RedactionService:

    @staticmethod
    def redact_text(text: str):
        return {
            "original_text": text,
            "redacted_text": text,
            "status": "success"
        }