import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class EnricherService:
    # SRP: única responsabilidad — enriquecer texto usando la API de Groq

    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def enrich_text(self, text: str) -> str:
        prompt = f"Amplía el siguiente texto sobre Wikipedia añadiendo contexto adicional, ejemplos o datos relevantes. Mantén un tono educativo y conciso: {text}"

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile"
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Ocurrió un error inesperado al enriquecer el texto: {e}")
            return text
