# Content Enrichment CLI

A command-line tool developed in Python to search information from Wikipedia, translate content into different languages and export results.

---

## Project Status

🚧 In development

Current features:

* Text translation using Deep Translator
* Command-line interaction
* Project structure prepared for Wikipedia integration

Planned features:

* Wikipedia scraping
* Content enrichment using OpenAI
* TXT export
* PDF generation
* Unit and integration tests

---

## What it does

The final objective of the project is:

1. Search a topic on Wikipedia
2. Extract the title and first five paragraphs
3. Enrich the content using AI
4. Translate the content into another language
5. Export the result as TXT or PDF

---

## Project Structure

```text
content-enrichment/
│
├── main.py
├── translator/
│   └── TranslatorServices.py
├── utils/
│   └── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tech Stack

| Tool            | Purpose            |
| --------------- | ------------------ |
| Python 3.14     | Main language      |
| requests        | HTTP requests      |
| BeautifulSoup4  | Wikipedia scraping |
| deep-translator | Translation        |
| OpenAI API      | Content enrichment |
| ReportLab       | PDF generation     |
| pytest          | Testing            |

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Irma0805/content-enrichment.git
cd content-enrichment
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Author

Irma

Back-end Development Bootcamp @ Factoría F5
