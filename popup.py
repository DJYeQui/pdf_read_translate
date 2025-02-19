import tkinter as tk

class PopupWindow:
    def __init__(self, text_original, text_translated, duration=15000):
        """ OCR ile okunan metni ve çevirisini ekranda gösterir. """

        self.root = tk.Toplevel()
        self.root.title("Çeviri Sonucu")
        self.root.configure(bg="white")
        self.root.attributes("-topmost", True)  # Popup pencereyi en üste getir
        self.root.overrideredirect(True)  # Kenarlıkları kaldır

        # Maksimum genişlik ayarı
        max_width = 700  # Pencere genişliği sabit
        padding_x = 2
        padding_y = 2

        # Dinamik olarak metin boyutunu hesapla
        original_lines = self.split_text(text_original, max_width - 40)
        translated_lines = self.split_text(text_translated, max_width - 40)

        # Pencere yüksekliği, metin uzunluğuna göre hesaplanır
        min_height = 180  # Minimum yükseklik
        line_height = 30  # Satır başına yükseklik
        height = min_height + (len(original_lines) + len(translated_lines)) * line_height * 2

        # Sağ alt köşeye yerleştirme
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{max_width}x{height}+{screen_width - max_width - 20}+{screen_height - height - 40}")

        # Çerçeve efekti için gölge ekleyelim
        frame = tk.Frame(self.root, bg="white", padx=padding_x, pady=padding_y, relief="solid", bd=1)
        frame.pack(fill=tk.BOTH, expand=True)

        # Orijinal Metin
        tk.Label(frame, text="Orijinal Metin:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(frame, text=original_lines, bg="white", wraplength=max_width - 40, font=("Arial", 10)).pack(anchor="w")

        # Çeviri Metni
        tk.Label(frame, text="Çeviri:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
        tk.Label(frame, text=translated_lines, bg="white", wraplength=max_width - 40, font=("Arial", 10), fg="blue").pack(anchor="w")

        # Otomatik kapatma (varsayılan 5 saniye)
        self.root.after(duration, self.close)

    def close(self):
        """ Popup penceresini kapatır. """
        self.root.destroy()

    def split_text(self, text, max_width):
        """ Metni belirli bir genişliğe uygun şekilde satırlara böler. """
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 < max_width // 8:  # Ortalama kelime genişliği 8 piksel
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.strip())

        return lines
