from builtins import ValueError, float
import tkinter as tk
from math import pi

def hitung_luas():
    try:
        radius = float(entryRadius.get())
        luas = 4 * pi * radius**2
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas: {luas:.2f} satuan persegi')
    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        radius = float(entryRadius.get())
        volume = (4/3) * pi * radius**3
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, f'Volume: {volume:.2f} satuan kubik')
    except ValueError:
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Bola")
app.geometry('400x300')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelName = tk.Label(frame, text="Ibnu Risfai", font=('Arial', 14, 'bold'))
labelName.grid(row=0, column=0, columnspan=2, pady=10)

labelRadius = tk.Label(frame, text="Jari-Jari: ", font=('Arial', 12))
labelRadius.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entryRadius = tk.Entry(frame, font=('Arial', 12))
entryRadius.grid(row=1, column=1)

luasButton = tk.Button(frame, text="Hitung Luas", command=hitung_luas, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
luasButton.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
volumeButton.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

textVolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textVolume.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
