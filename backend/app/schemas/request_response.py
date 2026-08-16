from pydantic import BaseModel, Field


class RedactRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Clinical text containing PHI/PII",
        example="John Smith visited AIIMS Delhi on 12/07/2026."
    )


class RedactResponse(BaseModel):
    original_text: str = Field(
        example="John Smith visited AIIMS Delhi on 12/07/2026."
    )
    redacted_text: str = Field(
        example="Patient_001 visited Hospital_001 on <DATE>."
    )
    status: str = Field(
        example="success"
    )


class RestoreRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Pseudonymized clinical text",
        example="Patient_001 visited Hospital_001."
    )


class RestoreResponse(BaseModel):
    restored_text: str = Field(
        example="John Smith visited AIIMS Delhi."
    )
    status: str = Field(
        example="success"
    )

class DetectionEnttity(BaseModel):
    start : int
    end : int
    text : str
    entity_type : str
    normalized : str
    confidence : float

class DetectionResponse(BaseModel):
    entity : list[DetectionEnttity]
    status : str