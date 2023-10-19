import math

# Input jari-jari dan tinggi kerucut dari pengguna
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))

# Menghitung luas permukaan kerucut
luas_permukaan = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))

# Menghitung volume kerucut
volume = (1/3) * math.pi * jari_jari**2 * tinggi

# Menampilkan hasil perhitungan
print(f"Luas Permukaan Kerucut: {luas_permukaan:.2f}")
print(f"Volume Kerucut: {volume:.2f}")
