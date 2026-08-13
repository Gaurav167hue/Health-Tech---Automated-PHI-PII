from pydantic import BaseModel

class RedactionResponse(BaseModel):
    original_text: str
    redacted_text: str
    status: str


class RestoreResponse(BaseModel):
    restored_text: str
    status: str