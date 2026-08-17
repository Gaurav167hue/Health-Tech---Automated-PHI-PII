from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine


class NLPService:

    def __init__(self):

        # ==========================================
        # SPACY MODEL
        # ==========================================

        models = [
            {
                "lang_code": "en",
                "model_name": "en_core_web_lg"
            }
        ]

        # ==========================================
        # SPACY NLP ENGINE
        # ==========================================

        nlp_engine = SpacyNlpEngine(
            models=models
        )

        # ==========================================
        # PRESIDIO ANALYZER
        # ==========================================

        self.analyzer = AnalyzerEngine(
            nlp_engine=nlp_engine
        )

    def analyze(
        self,
        text: str,
        entities: list[str] | None = None,
        language: str = "en"
    ):

        return self.analyzer.analyze(
            text=text,
            entities=entities,
            language=language
        )


# ==========================================
# SINGLE NLP SERVICE INSTANCE
# ==========================================

nlp_service = NLPService()

analyzer = nlp_service.analyzer