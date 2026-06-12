import os
from src.exporter.FileExporter import FileExporter


def test_export_creates_txt_file():
    exporter = FileExporter()
    exporter.export("contenido de prueba", "test_file", "txt")

    assert os.path.exists("output/test_file.txt")

    os.remove("output/test_file.txt")

def test_export_creates_pdf_file():
    exporter = FileExporter()
    exporter.export("contenido de prueba", "test_file", "pdf")

    assert os.path.exists("output/test_file.pdf")

    os.remove("output/test_file.pdf")

def test_export_does_nothing_when_format_is_invalid ():
    exporter = FileExporter()
    exporter.export("contenido de prueba", "test_file", "xyz")
    assert not os.path.exists("output/test_file.txt")
