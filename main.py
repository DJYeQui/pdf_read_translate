import tkinter as tk
import pyautogui
import keyboard
import threading
import queue
from read_png import ReadDocuments
from popup import PopupWindow  # Yeni popup class'ı içe aktar

event_queue = queue.Queue()

def open_screenshot_tool():
    """ Ekran görüntüsü alma aracını açar. """
    event_queue.put("start")

def run_tkinter_app():
    """ Ana thread içinde çalışır ve event_queue'yi kontrol eder. """
    root = tk.Tk()
    root.withdraw()

    def check_queue():
        try:
            while not event_queue.empty():
                event = event_queue.get_nowait()
                if event == "start":
                    show_screenshot_window()
        except queue.Empty:
            pass
        root.after(100, check_queue)

    def show_screenshot_window():
        """ Ekran görüntüsü seçme penceresini açar. """
        top = tk.Toplevel(root)
        top.overrideredirect(True)
        top.attributes("-topmost", True)
        top.attributes("-alpha", 0.3)

        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        top.geometry(f"{screen_width}x{screen_height}+0+0")

        canvas = tk.Canvas(top, cursor="cross", bg="black")
        canvas.pack(fill=tk.BOTH, expand=True)

        start_x, start_y = None, None
        rect = None

        def on_button_press(event):
            nonlocal start_x, start_y, rect
            start_x, start_y = event.x, event.y
            rect = canvas.create_rectangle(start_x, start_y, start_x, start_y,
                                           outline="red", width=2)

        def on_move_press(event):
            canvas.coords(rect, start_x, start_y, event.x, event.y)

        def on_button_release(event):
            top.destroy()

            x1, y1 = min(start_x, event.x), min(start_y, event.y)
            x2, y2 = max(start_x, event.x), max(start_y, event.y)

            screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
            screenshot.save("selected_area.png")

            # OCR işlemini başlat
            reader = ReadDocuments("selected_area.png")
            extracted_text = reader.read_png()

            print("Tespit Edilen Metin:")
            print(extracted_text)

            # Popup pencereyi aç
            PopupWindow(text_original=reader.extracted_text, text_translated=reader.translated_text)

        canvas.bind("<ButtonPress-1>", on_button_press)
        canvas.bind("<B1-Motion>", on_move_press)
        canvas.bind("<ButtonRelease-1>", on_button_release)

    root.after(100, check_queue)
    root.mainloop()

def start_hotkey_listener():
    """ Arka planda kısayol tuşunu dinler. """
    print("OCR için 'r' tuşuna basın...")
    keyboard.add_hotkey("r", open_screenshot_tool)
    keyboard.wait()

# Tkinter uygulamasını çalıştıran thread
tkinter_thread = threading.Thread(target=run_tkinter_app, daemon=True)
tkinter_thread.start()

# Kısayol dinleyicisini başlat
start_hotkey_listener()
