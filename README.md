# Content Enrichment CLI

Herramienta de línea de comandos desarrollada en Python que automatiza el proceso de buscar información en Wikipedia, enriquecerla con inteligencia artificial, traducirla al idioma elegido y exportarla a TXT o PDF.

---

## Estado del proyecto

| Historia | Descripción | Estado |
|---|---|---|
| HU-01 | Buscar información en Wikipedia | ✅ Completada |
| HU-02 | Traducir contenido | ✅ Completada |
| HU-03 | Gestión de errores | ✅ Completada |
| HU-04 | Guardar resultado en TXT | ✅ Completada |
| HU-05 | Exportar resultado en PDF | ✅ Completada |
| HU-06 | Enriquecer contenido con IA | ✅ Completada |
| HU-07 | Sistema de logs | ⏭ Mejora futura |

**Cobertura de tests:** 100% · 15 tests (13 unitarios + 2 de integración)

---

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3.14 | Lenguaje principal |
| requests | Peticiones HTTP a Wikipedia |
| BeautifulSoup4 | Parseo de HTML y extracción de contenido |
| Groq API (llama-3.3-70b-versatile) | Enriquecimiento con IA |
| deep-translator (GoogleTranslator) | Traducción (100+ idiomas) |
| ReportLab | Generación de archivos PDF |
| python-dotenv | Gestión segura de API keys |
| pytest + pytest-cov | Testing y cobertura |
| unittest.mock | Simulación de APIs en tests unitarios |

---

## Arquitectura

```
content-enrichment/
├── src/
│   ├── wikipedia/
│   │   ├── WikipediaClient.py     # Peticiones HTTP a Wikipedia
│   │   ├── WikipediaParser.py     # Extracción de título y párrafos
│   │   └── WikipediaScraper.py    # Orquesta Client y Parser
│   ├── translator/
│   │   └── TranslatorServices.py  # Traducción con GoogleTranslator
│   ├── enricher/
│   │   └── EnricherService.py     # Enriquecimiento con Groq API
│   ├── exporter/
│   │   └── FileExporter.py        # Exportación a TXT y PDF
│   └── utils/
│       └── utils.py               # get_user_input()
├── tests/
│   ├── unit/                      # Tests aislados con patch/MagicMock
│   └── integration/               # Tests con llamadas reales a Wikipedia
├── app.py                         # Clase App — orquestador del pipeline
├── main.py                        # Punto de entrada
├── config.py                      # Constantes (WIKIPEDIA_BASE_URL)
├── .env                           # API keys (no se sube a GitHub)
├── .env.example                   # Plantilla de configuración
└── requirements.txt
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Irma0805/content-enrichment.git
cd content-enrichment
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API key de Groq

Copia el archivo `.env.example` y añade tu API key:

```bash
cp .env.example .env
```

Edita `.env`:

```
GROQ_API_KEY=tu_api_key_aqui
```

Puedes obtener una API key gratuita en [console.groq.com](https://console.groq.com).

---

## Uso

```bash
python main.py
```

El programa guía al usuario paso a paso:

```
¿Sobre qué tema quieres buscar? Madrid
¿A qué idioma quieres traducir el contenido? (ej: en, fr, de) en

Título: Madrid
[contenido de Wikipedia...]

¿Quieres enriquecer el contenido con IA? (s/n) s
[contenido enriquecido por Groq...]

[contenido traducido al inglés...]

¿Quieres guardar el resultado en un archivo? (s/n) s
¿Qué nombre quieres darle al archivo? madrid
¿En qué formato lo quieres guardar? (txt/pdf) pdf

Archivo guardado como output/madrid.pdf
```

Los archivos se guardan en la carpeta `output/` (creada automáticamente).

El archivo exportado contiene tres secciones:
- `===CONTENIDO ORIGINAL===` — texto extraído de Wikipedia
- `===CONTENIDO ENRIQUECIDO===` — texto ampliado por la IA
- `===CONTENIDO TRADUCIDO===` — texto traducido al idioma elegido

---

## Tests

```bash
# Ejecutar todos los tests con cobertura
pytest tests/ -v --cov=src --cov-report=term-missing

# Solo tests unitarios
pytest tests/unit/ -v

# Solo tests de integración (requiere conexión a internet)
pytest tests/integration/ -v
```

---

## Principios de diseño

- **SRP** — cada archivo tiene una sola responsabilidad
- **KISS** — soluciones simples sobre complejidad innecesaria
- **DRY** — constantes centralizadas en `config.py`, utilidades reutilizables
- **YAGNI** — solo se implementó lo que el proyecto requería

---

## Mejoras futuras

- **HU-07** — sistema de logs con módulo `logging` de la librería estándar
- Preguntar al usuario si desea traducir (actualmente siempre traduce)
- Soporte para más fuentes además de Wikipedia
- Caché de búsquedas para evitar peticiones repetidas
- Interfaz web con Flask o FastAPI

