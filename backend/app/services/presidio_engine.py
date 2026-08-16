from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider


NLP_CONFIGURATION = {
    "nlp_engine_name": "spacy",
    "models": [
        {
            "lang_code": "en",
            "model_name": "en_core_web_lg",
        }
    ],
}


provider = NlpEngineProvider(
    nlp_configuration=NLP_CONFIGURATION
)

nlp_engine = provider.create_engine()

analyzer = AnalyzerEngine(
    nlp_engine=nlp_engine,
    supported_languages=["en"],
)


def analyze(
    text: str,
    entities: list[str]
):
    return analyzer.analyze(
        text=text,
        entities=entities,
        language="en"
    )