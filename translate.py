from googletrans import Translator
import asyncio
class Translator_fatih:

    async def translate_text(self, text, src="auto", dest="tr"):
        translator = Translator()
        translation = await translator.translate(text, src=src, dest=dest)
        return translation.text


