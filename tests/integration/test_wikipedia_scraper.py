from src.wikipedia.WikipediaScraper import WikipediaScraper


def test_search_topic_returns_real_content_for_valid_topic():
    scraper = WikipediaScraper()
    result = scraper.search_topic("Python")

    assert result["title"] != ""
    assert len(result["paragraphs"]) == 5


def test_search_topic_returns_empty_for_nonexistent_topic():
    scraper = WikipediaScraper()
    result = scraper.search_topic("xyzabc123nonexistent")

    assert result == {}