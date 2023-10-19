def luas_prisma_segitiga(alas, tinggi):
    luas_segitiga = 0.5 * alas * tinggi
    return 2 * luas_segitiga

def volume_prisma_segitiga(alas, tinggi, tinggi_prisma):
    luas_segitiga = 0.5 * alas * tinggi
    volume = luas_segitiga * tinggi_prisma
    return volume

# Input alas dan tinggi segitiga
print("menghitung luas dan volume prisma segitiga")
print("_________________________________________________")
alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))

# Input tinggi prisma
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Hitung luas dan volume prisma segitiga
luas = luas_prisma_segitiga(alas_segitiga, tinggi_segitiga)
volume = volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)

# Tampilkan hasil
print("hasil menghitung luas dan volume prisma segitiga")
print("_________________________________________________")
print(f"Luas prisma segitiga adalah: {luas}")
print(f"Volume prisma segitiga adalah: {volume}")
