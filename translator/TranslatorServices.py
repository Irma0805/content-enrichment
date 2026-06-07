from deep_translator import GoogleTranslator

class TranslatorService:
    #método constructor
    def __init__(self):
        pass

    def translate_text(self, text:str, source_lang:str, target_lang:str):
        try:
            translated_text = GoogleTranslator(
                source=source_lang,
                target=target_lang
            ).translate(text)
            return translated_text
        except Exception as e:
            print(f"An unexpected error ocurred: {e}")



#print(translate_text('soy programadora y muy genial', source_lang ='auto', target_lang ='en'))
#print(translate_text('amor mío, te amo', source_lang = 'auto', target_lang ='fr'))
#print(translate_text('cambiaron a Nana', source_lang ='auto', target_lang ='nl'))



