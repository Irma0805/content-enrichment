import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class FileExporter:
    # SRP: única responsabilidad — exportar contenido a archivos TXT o PDF

    def export(self, content: str, filename: str, file_format: str):
        os.makedirs("output", exist_ok=True)

        if file_format == "txt":
            self._export_to_txt(content, filename)
        elif file_format == "pdf":
            self._export_to_pdf(content, filename)
        else:
            print(f"Formato no soportado: {file_format}")

    def _export_to_txt(self, content: str, filename: str):
        with open(f"output/{filename}.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Archivo guardado como output{filename}.txt")

    def _export_to_pdf(self, content: str, filename: str):
        doc = SimpleDocTemplate(f"output/{filename}.pdf", pagesize=A4)
        styles = getSampleStyleSheet()
        paragraph = Paragraph(content, styles["Normal"])
        doc.build([paragraph])
        print(f"Archivo guardado como output/{filename}.pdf")