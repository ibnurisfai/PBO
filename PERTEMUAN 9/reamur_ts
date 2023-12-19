def reamur_to_kelvin(reamur):
    return reamur / 0.8 + 273.15

def reamur_to_celsius(reamur):
    return reamur / 0.8

def reamur_to_fahrenheit(reamur):
    return (reamur / 0.8) * 9/5 + 32

def main():
    try:
        reamur_temp = float(input("Enter temperature in Reamur: "))

        kelvin_temp = reamur_to_kelvin(reamur_temp)
        celsius_temp = reamur_to_celsius(reamur_temp)
        fahrenheit_temp = reamur_to_fahrenheit(reamur_temp)

        print(f"\nTemperature in Kelvin: {kelvin_temp:.2f} K")
        print(f"Temperature in Celsius: {celsius_temp:.2f} °C")
        print(f"Temperature in Fahrenheit: {fahrenheit_temp:.2f} °F")

    except ValueError:
        print("Please enter a valid temperature!")

if __name__ == "__main__":
    main()
