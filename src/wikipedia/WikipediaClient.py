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
                print(f"Página no encontrada: {url}")
                return ""

            return response.text

        except requests.exceptions.ConnectionError:
            print("No hay conexión a internet.")
            return ""

        except requests.exceptions.RequestException as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            return ""


