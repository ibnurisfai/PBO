class KonversiSuhu:
    def __init__(self, suhu_reamur):
        self.suhu_reamur = suhu_reamur

    def reamur_to_celsius(self):
        return self.suhu_reamur * 5/4

    def reamur_to_fahrenheit(self):
        celsius = self.reamur_to_celsius()
        return celsius * 9/5 + 32

    def reamur_to_kelvin(self):
        celsius = self.reamur_to_celsius()
        return celsius + 273.15

# Contoh penggunaan
suhu_reamur = 25
konversi = KonversiSuhu(suhu_reamur)

print(f"{suhu_reamur} Reamur setara dengan:")
print(f"{konversi.reamur_to_celsius():.2f} Celsius")
print(f"{konversi.reamur_to_fahrenheit():.2f} Fahrenheit")
print(f"{konversi.reamur_to_kelvin():.2f} Kelvin")
