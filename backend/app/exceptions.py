from fastapi import HTTPException


def invalid_request(message: str):
    raise HTTPException(
        status_code=400,
        detail=message
    )