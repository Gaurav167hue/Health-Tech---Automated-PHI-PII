from fastapi import APIRouter
from app.schemas.request_response import RedactRequest, RedactResponse

router = APIRouter(prefix="/api/v1", tags=["Redaction"])


@router.post("/redact", response_model=RedactResponse)
def redact_text(request: RedactRequest):

    return RedactResponse(
        original_text=request.text,
        redacted_text=request.text,
        status="success"
    )0000