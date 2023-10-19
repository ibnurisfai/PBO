import math
import math

def hitung_luas_permukaan(jari_jari):
    luas = 4 * math.pi * jari_jari**2
    return luas

def hitung_volume(jari_jari):
    volume = (4/3) * math.pi * jari_jari**3
    return volume

def main():
    jari_jari = float(input("Masukkan jari-jari bola: "))

    luas_permukaan = hitung_luas_permukaan(jari_jari)
    volume = hitung_volume(jari_jari)

    print(f"Luas Permukaan Bola: {luas_permukaan:.2f}")
    print(f"Volume Bola: {volume:.2f}")

if __name__ == "__main__":
    main()
