from unittest.mock import patch, MagicMock
from src.enricher.EnricherService import EnricherService


def test_enrich_text_returns_enriched_content_when_api_succeeds():
    service = EnricherService()

    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Texto enriquecido por la IA"

    with patch.object(service.client.chat.completions, "create", return_value=mock_response):
        result = service.enrich_text("Texto original")

    assert result == "Texto enriquecido por la IA"

def test_enrich_text_returns_original_text_when_api_fails():
    service = EnricherService()

    with patch.object(service.client.chat.completions, "create", side_effect=Exception("API error")):
        result = service.enrich_text("Texto original")

    assert result == "Texto original"