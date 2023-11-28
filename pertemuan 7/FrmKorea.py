from googletrans import Translator
import tkinter as tk
from tkinter import Label, Text, Scrollbar, Button, RIGHT, Y, END

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Indonesian to Korean Translator")
        self.setup_gui()

    def setup_gui(self):
        self.label_input = Label(self.root, text="Input Text (Indonesian):")
        self.label_input.pack(pady=10)

        self.text_input = Text(self.root, height=5, width=40)
        self.text_input.pack(pady=10)

        self.label_output = Label(self.root, text="Output Text (Korean):")
        self.label_output.pack(pady=10)

        self.text_output = Text(self.root, height=5, width=40)
        self.text_output.pack(pady=10)

        scrollbar = Scrollbar(self.root, command=self.text_output.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_output.config(yscrollcommand=scrollbar.set)

        self.translate_button = Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

    def translate_text(self):
        translator = Translator()
        input_text = self.text_input.get("1.0", "end-1c")
        translation = translator.translate(input_text, src='id', dest='ko')  # Change 'ja' to 'ko' for Korean
        self.text_output.delete("1.0", END)
        self.text_output.insert("1.0", translation.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
