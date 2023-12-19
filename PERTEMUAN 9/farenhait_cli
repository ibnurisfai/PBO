import sys

def convert_fahrenheit(fahrenheit):
    """Konversi suhu dari Fahrenheit ke Celcius, Reamur, dan Kelvin."""
    # Konversi ke Celcius
    celcius = (fahrenheit - 32) * 5 / 9
    # Konversi ke Reamur
    reamur = 4 / 5 * celcius
    # Konversi ke Kelvin
    kelvin = celcius + 273

    return celcius, reamur, kelvin


def main():
    # Membaca suhu dalam Fahrenheit
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

    # Konversi suhu
    celcius, reamur, kelvin = convert_fahrenheit(fahrenheit)

    # Menampilkan hasil konversi
    print(f"Suhu {fahrenheit} Fahrenheit sama dengan:")
    print(f"{celcius} Celcius")
    print(f"{reamur} Reamur")
    print(f"{kelvin} Kelvin")


if __name__ == "__main__":
    main()
