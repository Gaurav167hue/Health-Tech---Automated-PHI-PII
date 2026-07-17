from pydantic import BaseModel, Field


class RedactRequest(BaseModel):
    text: str = Field(
        ...,
        example="John Smith visited AIIMS Delhi on 12/07/2026."
    )


class RedactResponse(BaseModel):
    original_text: str
    redacted_text: str
    status: str


class RestoreRequest(BaseModel):
    text: str = Field(
        ...,
        example="Patient_001 visited Hospital_001."
    )


class RestoreResponse(BaseModel):
    restored_text: str
    status: str