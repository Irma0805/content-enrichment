from src.wikipedia.WikipediaScraper import WikipediaScraper
from src.translator.TranslatorServices import TranslatorService
from src.enricher.EnricherService import EnricherService
from src.utils.utils import get_user_input
from src.exporter.FileExporter import FileExporter


class App:
    # SRP: única responsabilidad — orquestar el pipeline completo de la app

    def __init__(self):
        self.scraper = WikipediaScraper()
        self.translator = TranslatorService()
        self.enricher = EnricherService()
        self.exporter = FileExporter()

        self.result = {}
        self.enriched_text = ""
        self.translated_text = ""

    def run(self):
        topic = get_user_input("¿Sobre qué tema quieres buscar? ")
        tgt_lang = get_user_input("¿A qué idioma quieres traducir el contenido? (ej: en, fr, de) ")

        self.result = self.scraper.search_topic(topic)
        if not self.result:
            print("No se pudo obtener el contenido. Saliendo.")
            return

        print(f"\nTítulo: {self.result['title']}")
        for p in self.result["paragraphs"]:
            print(p)

        full_text = "\n".join(self.result["paragraphs"])

        enrich = get_user_input("¿Quieres enriquecer el contenido con IA? (s/n) ")

        if enrich == "s":
            self.enriched_text = self.enricher.enrich_text(full_text)
            print(f"\nContenido enriquecido:\n{self.enriched_text}")
        else:
            self.enriched_text = full_text

        self.translated_text = self.translator.translate_text(self.enriched_text, "es", tgt_lang)
        print(f"\nContenido traducido:\n{self.translated_text}")

        save = get_user_input("¿Quieres guardar el resultado en un archivo? (s/n) ")
        if save =="s":
            filename = get_user_input("¿Qué nombre quieres darle al archivo? ")
            file_format = get_user_input("¿En qué formato lo quieres guardar? (txt/pdf) ")

            content = (f"Título: {self.result['title']}\n\n"
                       f"===CONTENIDO ORIGINAL===\n{self.original_text}\n\n"
                       f"===CONTENIDO ENRIQUECIDO===\n{self.enriched_text}\n\n"
                       f"===CONTENIDO TRADUCIDO===\n{self.translated_text}\n\n"
                       )
            self.exporter.export(content, filename, file_format)