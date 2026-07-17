from fastapi import APIRouter
from app.schemas.request_response import RedactRequest, RedactResponse
from app.services.redaction_service import RedactionService

router = APIRouter(
    prefix="/api/v1",
    tags=["Redaction"]
)


@router.post("/redact", response_model=RedactResponse)
def redact_text(request: RedactRequest):

    result = RedactionService.redact_text(request.text)

    return RedactResponse(**result)