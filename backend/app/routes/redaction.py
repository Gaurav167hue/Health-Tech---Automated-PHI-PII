from fastapi import APIRouter
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


@router.post("/redact", response_model=RedactResponse)
def redact_text(request: RedactRequest):
    result = RedactionService.redact_text(request.text)
    return RedactResponse(**result)


@router.post("/restore", response_model=RestoreResponse)
def restore_text(request: RestoreRequest):
    result = RedactionService.restore_text(request.text)
    return RestoreResponse(**result)