import tkinter as tk

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
    # Buat jendela
    root = tk.Tk()

    # Buat label dan entry untuk suhu Fahrenheit
    label_fahrenheit = tk.Label(root, text="Suhu dalam Fahrenheit:")
    entry_fahrenheit = tk.Entry(root)

    # Buat label dan text untuk suhu Celcius
    label_celcius = tk.Label(root, text="Celcius:")
    text_celcius = tk.Text(root, width=10, height=1)

    # Buat label dan text untuk suhu Reamur
    label_reamur = tk.Label(root, text="Reamur:")
    text_reamur = tk.Text(root, width=10, height=1)

    # Buat label dan text untuk suhu Kelvin
    label_kelvin = tk.Label(root, text="Kelvin:")
    text_kelvin = tk.Text(root, width=10, height=1)

    # Tata letak komponen
    label_fahrenheit.grid(row=0, column=0)
    entry_fahrenheit.grid(row=0, column=1)
    label_celcius.grid(row=1, column=0)
    text_celcius.grid(row=1, column=1)
    label_reamur.grid(row=2, column=0)
    text_reamur.grid(row=2, column=1)
    label_kelvin.grid(row=3, column=0)
    text_kelvin.grid(row=3, column=1)

    # Event handler untuk tombol konversi
    def konversi():
        # Membaca suhu dalam Fahrenheit dari entry
        fahrenheit = float(entry_fahrenheit.get())

        # Konversi suhu
        celcius, reamur, kelvin = convert_fahrenheit(fahrenheit)

        # Menampilkan hasil konversi
        text_celcius.delete(1.0, tk.END)
        text_celcius.insert(1.0, f"{celcius}")
        text_reamur.delete(1.0, tk.END)
        text_reamur.insert(1.0, f"{reamur}")
        text_kelvin.delete(1.0, tk.END)
        text_kelvin.insert(1.0, f"{kelvin}")

    # Buat tombol konversi
    button_konversi = tk.Button(root, text="Konversi", command=konversi)
    button_konversi.grid(row=4, column=0, columnspan=2)

    # Jalankan jendela
    root.mainloop()


if __name__ == "__main__":
    main()
