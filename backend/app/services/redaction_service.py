from app.exceptions import invalid_request


class RedactionService:

    @staticmethod
    def redact_text(text: str):

        if not text.strip():
            invalid_request("Input text cannot be empty.")

        return {
            "original_text": text,
            "redacted_text": text,
            "status": "success"
        }