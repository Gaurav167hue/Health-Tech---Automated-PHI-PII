from fastapi import FastAPI
from app.routes.redaction import router as redaction_router
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #develoment only, change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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