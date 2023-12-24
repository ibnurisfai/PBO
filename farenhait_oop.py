class TemperatureConverter:

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def get_celsius(self):
        return (self.fahrenheit - 32) * 5 / 9

    def get_reamur(self):
        return 4 / 5 * self.get_celsius()

    def get_kelvin(self):
        return self.get_celsius() + 273

    def __str__(self):
        return f"{self.fahrenheit} Fahrenheit"


def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    converter = TemperatureConverter(fahrenheit)

    print(f"\n{converter}")
    print(f"Celcius: {converter.get_celsius():.2f}")
    print(f"Reamur: {converter.get_reamur():.2f}")
    print(f"Kelvin: {converter.get_kelvin():.2f}")


if __name__ == "__main__":
    main()
