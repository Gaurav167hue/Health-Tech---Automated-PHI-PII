from fastapi import APIRouter, status
from app.schemas.request_response import (
    RedactRequest,
    RedactResponse,
    RestoreRequest,
    RestoreResponse,
    DetectionEnttity,
    DetectionResponse,
)
from app.services.redaction_service import RedactionService

# member 2
from app.services.detection_service import DetectionService

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

# member 2
@router.post(
    "/detect",
    response_model=DetectionResponse,
    status_code= status.HTTP_200_OK,
    summary="Detect PHI/PII",
    description="Detect PHI/PII Entity from Text"
)
def detect_text(request: RedactRequest):
    result = DetectionService.detect(request.text)
    return DetectionResponse(
        entity=  result,
        status= "succes"
    )
