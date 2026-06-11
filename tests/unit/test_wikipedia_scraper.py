from unittest.mock import patch
from src.wikipedia.WikipediaScraper import WikipediaScraper


def test_search_topic_returns_empty_when_unexpected_error_occurs():
    scraper = WikipediaScraper()
    with patch("src.wikipedia.WikipediaScraper.WikipediaParser.parse") as mock_parse:
        mock_parse.side_effect = Exception("Parsing failed")
        result = scraper.search_topic("Python")
        assert result == {}