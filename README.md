# 📚 EasyTranslateReader

**EasyTranslateReader** is a desktop application developed to eliminate the disruption caused by frequently switching to translation tools while reading English books or articles. With a single hotkey, the user can select any region of the screen, extract the text using OCR, translate it into Turkish, and display both the original and translated text in a popup window — all within seconds.

## 🚀 Project Purpose

This project aims to improve the reading experience for non-native English speakers by providing a quick and seamless way to translate any text on the screen. It also served as a great opportunity to practice basic **multi-threading** and **GUI programming** in Python.

## ⚙️ Technologies Used

- **Python**
- **Tkinter** – For GUI and popup windows
- **PyAutoGUI** – To capture screen regions
- **pytesseract** – For OCR (Optical Character Recognition)
- **Google Translate (googletrans)** – For text translation
- **Threading & Queue** – For running background tasks without freezing the UI

## 🧩 Project Structure

- `main.py`: Main application logic, listens for hotkeys and handles screenshot selection.
- `read_png.py`: Performs OCR on the captured image and initiates translation.
- `popup.py`: Creates a popup window displaying both the original and translated text.
- `translate.py`: Uses Google Translate API to translate the extracted text asynchronously.

## 🖥️ How It Works

1. The application runs in the background after launch.
2. Pressing the `r` key allows the user to select any area on the screen.
3. The selected region is saved as `selected_area.png`.
4. OCR is applied to extract the text from the image.
5. The extracted text is automatically translated into Turkish.
6. Both the original and translated text are shown in a popup window.

## 🧠 What I Learned

- Gained hands-on experience with threads to keep the GUI responsive.
- Learned how to combine OCR and translation to solve a real-world problem.
- Designed a simple but effective user interface focused on usability.

## ⚠️ Notes

- **Tesseract OCR** must be installed and properly configured (Default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`).
- The `googletrans` library may occasionally face connection or quota issues — be aware of its limitations.

## ✨ Future Improvements

- Add support for multiple translation directions (e.g., Turkish → English)
- Allow saving of translated words for vocabulary practice
- UI improvements and optional dark mode
- Better error handling and user feedback

---
