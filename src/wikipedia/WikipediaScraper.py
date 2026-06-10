from config import WIKIPEDIA_BASE_URL
from src.wikipedia.WikipediaClient import WikipediaClient
from src.wikipedia.WikipediaParser import WikipediaParser


class WikipediaScraper:
    # SRP: única responsabilidad — orquestar Client y Parser

    def __init__(self):
        self.client = WikipediaClient()
        self.parser = WikipediaParser()

    def build_url(self, topic: str) -> str:
        return WIKIPEDIA_BASE_URL + topic.replace(" ", "_")


    def search_topic(self, topic: str) -> dict:
        try:
            html = self.client.get_page(self.build_url(topic))
            if not html:
                return {}
            return self.parser.parse(html)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}