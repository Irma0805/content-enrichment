from src.wikipedia.WikipediaParser import WikipediaParser


def test_parse_returns_title_and_paragraphs_when_html_is_valid():
    html = """
    <html>
        <h1>Python</h1>
        <p>First paragraph about Python.</p>
        <p>Second paragraph about Python.</p>
        <p>Third paragraph about Python.</p>
        <p>Fourth paragraph about Python.</p>
        <p>Fifth paragraph about Python.</p>
        <p>Sixth paragraph that should be ignored.</p>
    </html>
    """
    parser = WikipediaParser()
    result = parser.parse(html)

    assert result["title"] == "Python"
    assert len(result["paragraphs"]) == 5
    assert result["paragraphs"][0] == "First paragraph about Python."

def test_parse_returns_empty_dict_when_no_title():
    html = "<html><p>Some paragraph without a title.</p></html>"
    parser = WikipediaParser()
    result = parser.parse(html)

    assert result == {}

def test_parse_returns_empty_dict_when_html_is_invalid_type():
    parser = WikipediaParser()
    result = parser.parse(None)

    assert result == {}