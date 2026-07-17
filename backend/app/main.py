from fastapi import FastAPI
from app.routes.redaction import router as redaction_router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.include_router(redaction_router)



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