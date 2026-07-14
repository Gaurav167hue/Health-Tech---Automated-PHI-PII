from fastapi import FastAPI
from app.routes.redaction import router as redaction_router

app = FastAPI(
    title="Health Redaction API",
    description="FastAPI service for PHI/PII Redaction Pipeline",
    version="1.0.0"
)

app.include_router(redaction_router)
)


@app.get("/")
def root():
    return {
        "message": "Health Redaction API is running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Health Redaction API",
        "version": "1.0.0"
    }