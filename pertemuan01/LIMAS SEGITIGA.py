import math

# Input panjang sisi-sisi segitiga
print("menghitung luas dan volume limas segitiga")
print("___________________________________________________")
sisi_a = float(input("Masukkan panjang sisi a segitiga: "))
sisi_b = float(input("Masukkan panjang sisi b segitiga: "))
sisi_c = float(input("Masukkan panjang sisi c segitiga: "))

# Input tinggi limas
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Hitung luas permukaan limas segitiga
luas_permukaan_segitiga = 0.5 * sisi_a * tinggi_limas + 0.5 * sisi_b * tinggi_limas + 0.5 * sisi_c * tinggi_limas
luas_permukaan_limas = luas_permukaan_segitiga + sisi_a * sisi_b + sisi_b * sisi_c + sisi_c * sisi_a

# Hitung volume limas segitiga
volume_limas = (1/3) * (sisi_a * sisi_b * tinggi_limas)

# Tampilkan hasil
print("Hasil menghitung luas dan volume limas segitiga")
print("___________________________________________________")
print("Luas permukaan limas segitiga adalah:", luas_permukaan_limas)
print("Volume limas segitiga adalah:", volume_limas)
