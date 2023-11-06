from builtins import ValueError, float
import tkinter as tk

def hitung_luas():
    try:
        panjang = float(entryPanjang.get())
        lebar = float(entryLebar.get())
        tinggi = float(entryTinggi.get())
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas: {luas:.2f} satuan persegi')
    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        panjang = float(entryPanjang.get())
        lebar = float(entryLebar.get())
        tinggi = float(entryTinggi.get())
        volume = panjang * lebar * tinggi
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, f'Volume: {volume:.2f} satuan kubik')
    except ValueError:
        textVolume.delete('1.0', tk.END)
        textVolume.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Balok")
app.geometry('400x400')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelPanjang = tk.Label(frame, text="Panjang: ", font=('Arial', 12))
labelPanjang.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entryPanjang = tk.Entry(frame, font=('Arial', 12))
entryPanjang.grid(row=0, column=1)

labelLebar = tk.Label(frame, text="Lebar: ", font=('Arial', 12))
labelLebar.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entryLebar = tk.Entry(frame, font=('Arial', 12))
entryLebar.grid(row=1, column=1)

labelTinggi = tk.Label(frame, text="Tinggi: ", font=('Arial', 12))
labelTinggi.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

entryTinggi = tk.Entry(frame, font=('Arial', 12))
entryTinggi.grid(row=2, column=1)

luasButton = tk.Button(frame, text="Hitung Luas", command=hitung_luas, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
luasButton.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
volumeButton.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

textVolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textVolume.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
