import requests
from unittest.mock import patch, MagicMock
from src.wikipedia.WikipediaClient import WikipediaClient


def test_get_page_returns_html_when_topic_is_valid():
    client = WikipediaClient()
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(status_code=200, text="<html><h1>Python</h1></html>")
        result = client.get_page("Python")
        assert result == "<html><h1>Python</h1></html>"


def test_get_page_returns_empty_when_topic_not_found():
    client = WikipediaClient()
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(status_code=404)
        result = client.get_page("xyzabc123")
        assert result == ""


def test_get_page_returns_empty_when_no_connection():
    client = WikipediaClient()
    with patch("src.wikipedia.WikipediaClient.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        result = client.get_page("https://en.wikipedia.org/wiki/Python")
        assert result == ""

def test_get_page_returns_empty_when_request_fails():
    client = WikipediaClient()
    with patch("src.wikipedia.WikipediaClient.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Request failed")
        result = client.get_page("https://en.wikipedia.org/wiki/Python")
        assert result == ""