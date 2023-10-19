import math

# Input panjang, lebar, tinggi, dan panjang sisi miring segitiga alas
panjang = float(input("Masukkan panjang segiempat: "))
lebar = float(input("Masukkan lebar segiempat: "))
tinggi = float(input("Masukkan tinggi limas: "))
panjang_sisi_miring = float(input("Masukkan panjang sisi miring segitiga alas: "))

# Hitung luas permukaan limas segiempat
luas_permukaan = (panjang * lebar) + (0.5 * panjang_sisi_miring * lebar * 4) + (0.5 * panjang_sisi_miring * tinggi)

# Hitung volume limas segiempat
volume = (1/3) * (panjang * lebar * tinggi)

# Tampilkan hasil
print("hasil perhitungan Luas dan volume Limas Segiempat")
print("_______________________________________________________")
print("Luas Permukaan Limas Segiempat: {:.2f}".format(luas_permukaan))
print("Volume Limas Segiempat: {:.2f}".format(volume))
