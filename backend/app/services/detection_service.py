from app.services.detectors.regex.phone_detector import detect_phone
from app.services.detectors.regex.email_detector import detect_email
from app.services.detectors.regex.date_detector import detect_date

class DetectionService:

    @staticmethod
    def detect(text: str):

        entities = []

        # =========================
        # REGEX DETECTION
        # =========================

        phone_entities = detect_phone(text)
        email_entities = detect_email(text)
        date_entities = detect_date(text)

        entities.extend(phone_entities)
        entities.extend(email_entities)
        entities.extend(date_entities)

        # =========================
        # PRESIDIO DETECTION
        # =========================


        # =========================
        # SORT BY POSITION
        # =========================

        entities.sort(
            key=lambda entity: entity["start"]
        )

        return entities