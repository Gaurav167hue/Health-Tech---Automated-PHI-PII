from pydantic import BaseModel


class RedactRequest(BaseModel):
    text: str


class RedactResponse(BaseModel):
    original_text: str
    redacted_text: str
    status: str 