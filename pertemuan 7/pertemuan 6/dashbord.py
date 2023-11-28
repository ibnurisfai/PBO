from googletrans import Translator
import tkinter as tk
from tkinter import Label, Text, Scrollbar, Button, RIGHT, Y, END, Menu

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")
        self.setup_gui()

    def setup_gui(self):
        # Menu
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        language_menu = Menu(menubar, tearoff=0)
        language_menu.add_command(label="Translate to Japanese", command=lambda: self.translate_text("ja"))
        language_menu.add_command(label="Translate to Korean", command=lambda: self.translate_text("ko"))
        language_menu.add_command(label="Translate to Chinese", command=lambda: self.translate_text("zh-CN"))
        menubar.add_cascade(label="Translate", menu=language_menu)

        # GUI components
        self.label_input = Label(self.root, text="Input Text (Indonesian):")
        self.label_input.pack(pady=10)

        self.text_input = Text(self.root, height=5, width=40)
        self.text_input.pack(pady=10)

        self.label_output = Label(self.root, text="Output Text:")
        self.label_output.pack(pady=10)

        self.text_output = Text(self.root, height=5, width=40)
        self.text_output.pack(pady=10)

        scrollbar = Scrollbar(self.root, command=self.text_output.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_output.config(yscrollcommand=scrollbar.set)

        self.translate_button = Button(self.root, text="Translate", command=lambda: self.translate_text("ja"))
        self.translate_button.pack(pady=10)

    def translate_text(self, dest_lang):
        translator = Translator()
        input_text = self.text_input.get("1.0", "end-1c")
        translation = translator.translate(input_text, src='id', dest=dest_lang)
        self.text_output.delete("1.0", END)
        self.text_output.insert("1.0", translation.text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
