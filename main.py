from translator.TranslatorServices import TranslatorService
from utils.utils import get_user_input

#UI
text = get_user_input("What would you like to transalate?")
src_lang = get_user_input("What is the source language?")
tgt_lang = get_user_input("What is the target language?")

#instancia de la clase = 0BJETO DE CLASE-----aquí se está ejecutando el programa
translator = TranslatorService().translate_text(text, src_lang, tgt_lang)
print(translator)