import requests
from bs4 import BeautifulSoup

class WikipediaServices:
    def __init__(self):
        pass

    def build_url(self, topic: url):
        return self.BASE_URL + topic.replace(' ', '_')

    def fetch_page(self, topic: url) -> BeautifulSoup:
        pass

    def extract_content(self, html: url) -> BeautifulSoup:
        pass

    def search_topic(self,topic:str):
        pass