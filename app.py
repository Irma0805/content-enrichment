from src.wikipedia.WikipediaScraper import WikipediaScraper
from src.translator.TranslatorServices import TranslatorService
from src.utils.utils import get_user_input


class App:
    # SRP: única responsabilidad — orquestar el pipeline completo de la app

    def __init__(self):
        self.scraper = WikipediaScraper()
        self.translator = TranslatorService()
        # más adelante: self.enricher = EnricherService()
        # más adelante: self.exporter = FileExporter()

        self.result = {}
        self.translated_text = ""

    def run(self):
        topic = get_user_input("¿Sobre qué tema quieres buscar? ")
        tgt_lang = get_user_input("¿A qué idioma quieres traducir el contenido? (ej: en, fr, de) ")

        self.result = self.scraper.search_topic(topic)

        if not self.result:
            print("No se pudo obtener el contenido. Saliendo.")
            return

        print(f"\nTítulo: {self.result['title']}")
        print(f"\nContenido:\n")
        for p in self.result["paragraphs"]:
            print(p)

        full_text = "\n".join(self.result["paragraphs"])
        self.translated_text = self.translator.translate_text(full_text, "es", tgt_lang)
        print(f"\nContenido traducido:\n{self.translated_text}")