from src.wikipedia.WikipediaScraper import WikipediaScraper
from src.translator.TranslatorServices import TranslatorService
from src.utils.utils import get_user_input

# UI — recogida de datos del usuario
topic = get_user_input("¿Sobre qué tema quieres buscar? ")
tgt_lang = get_user_input("¿A qué idioma quieres traducir el contenido? (ej: en, fr, de) ")

# Paso 1 — Scraping
result = WikipediaScraper().search_topic(topic)

if not result:
    print("No se pudo obtener el contenido. Saliendo.")
else:
    print(f"\nTítulo: {result['title']}")
    print(f"\nContenido:\n")
    for p in result["paragraphs"]:
        print(p)

    # Paso 2 — Traducción
    full_text = "\n".join(result["paragraphs"])
    translator = TranslatorService().translate_text(full_text, "es", tgt_lang)
    print(f"\nContenido traducido:\n{translator}")