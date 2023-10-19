#INPUTAN BALOK
print("menghitung luas dan volume balok")
print("_________________________________")
panjang=float(input("masukan panjang balok: "))
lebar=float(input("masukan lebar balok: "))
tinggi=float(input("masukan tinggi balok: "))
#PROSES PERHITUNGAN
volume= panjang*lebar*tinggi
luas=2*(panjang*lebar+ panjang*tinggi+lebar*tinggi)
#TAMPILKAN DATA
print("volume balok adalah", volume)
print("Luas balok adalah",luas)