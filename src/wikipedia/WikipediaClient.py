import requests

class WikipediaClient:
    # SRP: única responsabilidad — hacer la petición HTTP a Wikipedia

    HEADERS = {
        "User-Agent": "ContentEnricher/1.0 (bootcamp project; educational use)"
    }

    def get_page(self, url: str) -> str:
        try:
            response = requests.get(url, headers=self.HEADERS)

            if response.status_code != 200:
                print(f"Page not found: {url}")
                return ""

            return response.text

        except requests.exceptions.ConnectionError:
            print("No internet connection available.")
            return ""

        except requests.exceptions.RequestException as e:
            print(f"An unexpected error occurred: {e}")
            return ""


