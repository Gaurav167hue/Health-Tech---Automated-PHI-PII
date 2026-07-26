from fastapi import APIRouter, status
from app.schemas.request_response import (
    RedactRequest,
    RedactResponse,
    RestoreRequest,
    RestoreResponse,
)
from app.services.redaction_service import RedactionService

router = APIRouter(
    prefix="/api/v1",
    tags=["Redaction"]
)

@router.post(
    "/redact",
    response_model=RedactResponse,
    status_code=status.HTTP_200_OK,
    summary="Redact PHI/PII",
    description="Accept clinical text and return the redacted version."
)
def redact_text(request: RedactRequest):
    result = RedactionService.redact_text(request.text)
    return RedactResponse(**result)

@router.post(
    "/restore",
    response_model=RestoreResponse,
    status_code=status.HTTP_200_OK,
    summary="Restore pseudonymized text",
    description="Restore the original clinical text from pseudonymized data."
)
def restore_text(request: RestoreRequest):
    result = RedactionService.restore_text(request.text)
    return RestoreResponse(**result)