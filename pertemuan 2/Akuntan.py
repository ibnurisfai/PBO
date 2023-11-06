import tkinter as tk

def hitung_laba_rugi():
    try:
        pendapatan = float(entryPendapatan.get())
        biaya = float(entryBiaya.get())
        laba_rugi = pendapatan - biaya
        labelLabaRugi.config(text=f'Laba Rugi: {laba_rugi:.2f} satuan')
    except ValueError:
        labelLabaRugi.config(text='Masukkan angka yang valid')

def hitung_laba_bersih():
    try:
        laba_kotor = float(entryLabaKotor.get())
        biaya_operasional = float(entryBiayaOperasional.get())
        pajak = float(entryPajak.get())
        laba_bersih = laba_kotor - biaya_operasional - pajak
        labelLabaBersih.config(text=f'Laba Bersih: {laba_bersih:.2f} satuan')
    except ValueError:
        labelLabaBersih.config(text='Masukkan angka yang valid')

def hitung_roa():
    try:
        laba_bersih = float(entryLabaBersihROA.get())
        total_aset = float(entryTotalAset.get())
        roa = laba_bersih / total_aset
        labelROA.config(text=f'ROA: {roa:.2f}')
    except ValueError:
        labelROA.config(text='Masukkan angka yang valid')

def hitung_roe():
    try:
        laba_bersih = float(entryLabaBersihROE.get())
        ekuitas = float(entryEkuitas.get())
        roe = laba_bersih / ekuitas
        labelROE.config(text=f'ROE: {roe:.2f}')
    except ValueError:
        labelROE.config(text='Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Keuangan")
app.geometry('400x600')

frame = tk.Frame(app, padx=40, pady=40)
frame.pack()

labelName = tk.Label(frame, text="KALKULATOR KEUANGAN", font=('Arial', 14, 'bold'))
labelName.grid(row=0, column=0, columnspan=1, pady=1)

# Untuk Laba Rugi
labelName = tk.Label(frame, text="Menghitung Labah Rugi", font=('Arial', 12))
labelName.grid(row=1, column=0, columnspan=2, pady=10)

labelPendapatan = tk.Label(frame, text="Pendapatan: ", font=('Arial', 12))
labelPendapatan.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

entryPendapatan = tk.Entry(frame, font=('Arial', 12))
entryPendapatan.grid(row=3, column=0)

labelBiaya = tk.Label(frame, text="Biaya: ", font=('Arial', 12))
labelBiaya.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

entryBiaya = tk.Entry(frame, font=('Arial', 12))
entryBiaya.grid(row=5, column=0)

labaRugiButton = tk.Button(frame, text="Hitung Laba Rugi", command=hitung_laba_rugi, font=('Arial', 12), bg='lightblue', padx=5, pady=5)
labaRugiButton.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

labelLabaRugi = tk.Label(frame, text="Laba Rugi: ", font=('Arial', 12))
labelLabaRugi.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Untuk Laba Bersih
labelName1 = tk.Label(frame, text="Menghitung Labah Bersih", font=('Arial', 12))
labelName1.grid(row=1, column=2, columnspan=1, pady=10)
labelLabaKotor = tk.Label(frame, text="Laba Kotor: ", font=('Arial', 12))
labelLabaKotor.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

entryLabaKotor = tk.Entry(frame, font=('Arial', 12))
entryLabaKotor.grid(row=3, column=2)

labelBiayaOperasional = tk.Label(frame, text="Biaya Operasional: ", font=('Arial', 12))
labelBiayaOperasional.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

entryBiayaOperasional = tk.Entry(frame, font=('Arial', 12))
entryBiayaOperasional.grid(row=5, column=2)

labelPajak = tk.Label(frame, text="Pajak: ", font=('Arial', 12))
labelPajak.grid(row=6, column=2, sticky=tk.W, padx=5, pady=5)

entryPajak = tk.Entry(frame, font=('Arial', 12))
entryPajak.grid(row=7, column=2)

labaBersihButton = tk.Button(frame, text="Hitung Laba Bersih", command=hitung_laba_bersih, font=('Arial', 12), bg='lightgreen', padx=5, pady=5)
labaBersihButton.grid(row=8, column=2, columnspan=1, padx=5, pady=5)

labelLabaBersih = tk.Label(frame, text="Laba Bersih: ", font=('Arial', 12))
labelLabaBersih.grid(row=9, column=2, columnspan=1, padx=5, pady=5)

# Untuk ROA
labelName2 = tk.Label(frame, text="Menghitung ROA", font=('Arial', 12))
labelName2.grid(row=1, column=3, columnspan=1, pady=10)
labelLabaBersihROA = tk.Label(frame, text="Laba Bersih: ", font=('Arial', 12))
labelLabaBersihROA.grid(row=2, column=3, sticky=tk.W, padx=5, pady=5)

entryLabaBersihROA = tk.Entry(frame, font=('Arial', 12))
entryLabaBersihROA.grid(row=3, column=3)

labelTotalAset = tk.Label(frame, text="Total Aset: ", font=('Arial', 12))
labelTotalAset.grid(row=4, column=3, sticky=tk.W, padx=5, pady=5)

entryTotalAset = tk.Entry(frame, font=('Arial', 12))
entryTotalAset.grid(row=5, column=3)

roaButton = tk.Button(frame, text="Hitung ROA", command=hitung_roa, font=('Arial', 12), bg='lightyellow', padx=5, pady=5)
roaButton.grid(row=6, column=3, columnspan=1, padx=5, pady=5)

labelROA = tk.Label(frame, text="ROA: ", font=('Arial', 12))
labelROA.grid(row=7, column=3, columnspan=1, padx=5, pady=5)

# Untuk ROE
labelName = tk.Label(frame, text=" Menghitung ROE", font=('Arial', 12))
labelName.grid(row=1, column=4, columnspan=2, pady=10)
labelLabaBersihROE = tk.Label(frame, text="Laba Bersih: ", font=('Arial', 12))
labelLabaBersihROE.grid(row=2, column=4, sticky=tk.W, padx=5, pady=5)

entryLabaBersihROE = tk.Entry(frame, font=('Arial', 12))
entryLabaBersihROE.grid(row=3, column=4)

labelTotalEkuitas = tk.Label(frame, text="Total Ekuitas: ", font=('Arial', 12))
labelTotalEkuitas.grid(row=4, column=4, sticky=tk.W, padx=5, pady=5)

entryEkuitas = tk.Entry(frame, font=('Arial', 12))
entryEkuitas.grid(row=5, column=4)

roeButton = tk.Button(frame, text="Hitung ROE", command=hitung_roe, font=('Arial', 12), bg='lightyellow', padx=5, pady=5)
roeButton.grid(row=6, column=4, columnspan=2, padx=5, pady=5)

labelROE = tk.Label(frame, text="ROE: ", font=('Arial', 12))
labelROE.grid(row=7, column=4, columnspan=2, padx=5, pady=5)

app.mainloop()