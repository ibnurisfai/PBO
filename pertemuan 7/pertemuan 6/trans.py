from tkinter import Frame, Label, Entry, Button, Tk, W, OptionMenu, StringVar
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill='both', expand='yes')

        # Pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Dari Bahasa:').grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # Pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=2, column=1, padx=5, pady=5)

        # Dropdown menu for language selection
        self.source_language_var = StringVar(mainFrame)
        self.source_language_var.set('id')  # Default language is Indonesian
        source_language_options = ['id', 'en', 'ja', 'ko', 'zh-CN']  # Added Japanese, Korean, and Chinese
        OptionMenu(mainFrame, self.source_language_var, *source_language_options).grid(row=1, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!', command=self.onTranslate)
        self.btnTranslate.grid(row=3, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # Clear previous results
        self.txtHasil.delete(0, 'end')

        # Get selected source language
        source_language = self.source_language_var.get()

        # Create translator instance
        penterjemah = Translator()

        # Translate
        hasil = penterjemah.translate(self.txtSumber.get(), src=source_language, dest='ja')  # Change 'ja' to the desired destination language

        # Display translation result
        self.txtHasil.insert('end', hasil.text)

    def onKeluar(self, event=None):
        # Close the application
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()
