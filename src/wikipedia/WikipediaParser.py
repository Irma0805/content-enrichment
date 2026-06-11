from bs4 import BeautifulSoup


class WikipediaParser:
    # SRP: única responsabilidad — extraer título y párrafos del HTML

    def parse(self, html: str) -> dict:
        try:
            soup = BeautifulSoup(html, "html.parser")

            title_tag = soup.find("h1")
            if not title_tag:
                print("Could not find title in the page.")
                return {}

            title = title_tag.text
            paragraphs = [
                p.text for p in soup.find_all("p")
                if p.text.strip()
            ][:5]

            return {"title": title, "paragraphs": paragraphs}

        except Exception as e:
            print(f"An unexpected error occurred while parsing: {e}")
            return {}