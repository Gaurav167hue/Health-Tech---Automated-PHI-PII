from app.services.nlp_service import analyzer

from app.services.detectors.regex.phone_detector import detect_phone
from app.services.detectors.regex.email_detector import detect_email
from app.services.detectors.regex.date_detector import detect_date
from app.services.detectors.regex.id_detector import detect_id

from app.services.detectors.presidio.person_detector import detect_person
from app.services.detectors.presidio.patient_detector import classify_patient
from app.services.detectors.presidio.doctor_detector import classify_doctor
from app.services.detectors.presidio.address_detector import detect_address
from app.services.detectors.presidio.context_detector import detect_context


class DetectionService:

    @staticmethod
    def detect(text: str):

        entities = []

        # ==========================================
        # 1. REGEX
        # ==========================================

        entities.extend(detect_phone(text))
        entities.extend(detect_email(text))
        entities.extend(detect_date(text))
        entities.extend(detect_id(text))

        # ==========================================
        # 2. PRESIDIO ANALYZER
        # ==========================================

        presidio_results = analyzer.analyze(
            text=text,
            entities=[
                "PERSON",
                "LOCATION"
            ],
            language="en"
        )

        # ==========================================
        # 3. PERSON
        # ==========================================

        person_results = detect_person(
            text,
            presidio_results
        )

        patient_entities = classify_patient(
            text,
            person_results
        )

        doctor_entities = classify_doctor(
            text,
            person_results
        )

        # ==========================================
        # 4. PERSON → DICT
        # ==========================================

        # RecognizerResult
        # for entity in patient_entities:

        #     value = text[
        #         entity.start:entity.end
        #     ].strip()

        #     entities.append({
        #         "start": entity.start,
        #         "end": entity.end,
        #         "text": value,
        #         "entity_type": "PATIENT",
        #         "normalized": value.lower(),
        #         "confidence": entity.score
        #     })

        # for entity in doctor_entities:

        #     value = text[
        #         entity.start:entity.end
        #     ].strip()

        #     entities.append({
        #         "start": entity.start,
        #         "end": entity.end,
        #         "text": value,
        #         "entity_type": "DOCTOR",
        #         "normalized": value.lower(),
        #         "confidence": entity.score
        #     })

        entities.extend(patient_entities)
        entities.extend(doctor_entities)

        # ==========================================
        # 5. ADDRESS
        # ==========================================

        address_entities = detect_address(
            text,
            presidio_results
        )

        entities.extend(address_entities)

        # ==========================================
        # 6. MEDICAL CONTEXT
        # ==========================================

        entities.extend(
            detect_context(text)
        )

        # ==========================================
        # 7. SORT
        # ==========================================

        entities.sort(
            key=lambda entity: entity["start"]
        )

        return entities