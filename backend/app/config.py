from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Health Redaction API")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    APP_DESCRIPTION = os.getenv(
        "APP_DESCRIPTION",
        "Automated PHI/PII Redaction Pipeline API"
    )
    DEBUG = os.getenv("DEBUG", "True")


settings = Settings()