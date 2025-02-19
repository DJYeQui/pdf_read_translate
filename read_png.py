import pytesseract
from PIL import Image
import asyncio
from translate import Translator_fatih

class ReadDocuments:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.extracted_text = ""
        self.r = ""

    def read_png(self) -> str:
        """
        PNG dosyasındaki metni OCR ile okur ve Türkçeye çevirir.
        """
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        image = Image.open(self.pdf_path)
        self.extracted_text = pytesseract.image_to_string(image).strip()

        print("Tespit Edilen Metin:")
        print(self.extracted_text)

        if not self.extracted_text:
            self.translated_text = "OCR işlemi başarısız oldu veya metin bulunamadı."
        else:
            translate_obj = Translator_fatih()
            self.translated_text = asyncio.run(translate_obj.translate_text(self.extracted_text, src="auto", dest="tr"))

        return self.translated_text
