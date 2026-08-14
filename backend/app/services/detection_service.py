from app.services.detectors.regex.phone_detector import detect_phone

class DetectionService:

    @staticmethod
    def detect(text: str):

        entities = []

        # =========================
        # REGEX DETECTION
        # =========================

        phone_entities = detect_phone(text)

        entities.extend(phone_entities)

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