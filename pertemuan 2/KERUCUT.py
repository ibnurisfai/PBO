from builtins import ValueError, float
import tkinter as tk
from tkinter import Label, Entry, Button, END, W
from math import pi, sqrt

def hitung_luas():
    try:
        radius = float(entryRadius.get())
        height = float(entryHeight.get())
        s = sqrt(radius ** 2 + height ** 2)
        luas = pi * radius * s
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas: {luas:.2f} satuan persegi')
    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        radius = float(entryRadius.get())
        height = float(entryHeight.get())
        volume = (1 / 3) * pi * radius ** 2 * height
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, f'Volume: {volume:.2f} satuan kubik')
    except ValueError:
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, 'Masukkan angka yang valid')

def hitung_luas_selimut():
    try:
        radius = float(entryRadius.get())
        height = float(entryHeight.get())
        s = sqrt(radius ** 2 + height ** 2)
        luas_selimut = pi * radius * s
        textLuasSelimut.delete('1.0', tk.END)
        textLuasSelimut.insert(tk.END, f'Luas Selimut: {luas_selimut:.2f} satuan persegi')
    except ValueError:
        textLuasSelimut.delete('1.0', tk.END)
        textLuasSelimut.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Kerucut")
app.geometry('400x500')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelName = tk.Label(frame, text="Ibnu Risfai", font=('Arial', 14, 'bold'))
labelName.grid(row=0, column=0, columnspan=2, pady=10)

labelRadius = tk.Label(frame, text="Jari-Jari: ", font=('Arial', 12))
labelRadius.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entryRadius = tk.Entry(frame, font=('Arial', 12))
entryRadius.grid(row=1, column=1)

labelHeight = tk.Label(frame, text="Tinggi: ", font=('Arial', 12))
labelHeight.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

entryHeight = tk.Entry(frame, font=('Arial', 12))
entryHeight.grid(row=2, column=1)

luasButton = tk.Button(frame, text="Hitung Luas", command=hitung_luas, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
luasButton.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
volumeButton.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

luasSelimutButton = tk.Button(frame, text="Hitung Luas Selimut", command=hitung_luas_selimut, font=('Arial', 12), bg='lightyellow', padx=5, pady=5)
luasSelimutButton.grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

textVolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textVolume.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

textLuasSelimut = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuasSelimut.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
