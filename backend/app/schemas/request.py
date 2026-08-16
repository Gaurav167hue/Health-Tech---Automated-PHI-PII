from pydantic import BaseModel, Field

class RedactionRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        example="Patient John Smith visited Dr. Adams on 12/03/2025."
    )