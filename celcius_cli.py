def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_reamur(celsius):
    return celsius * 0.8

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        celsius_temp = float(input("Enter temperature in Celsius: "))

        kelvin_temp = celsius_to_kelvin(celsius_temp)
        reamur_temp = celsius_to_reamur(celsius_temp)
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

        print(f"Temperature in Kelvin: {kelvin_temp:.2f} K")
        print(f"Temperature in Reamur: {reamur_temp:.2f} Reamur")
        print(f"Temperature in Fahrenheit: {fahrenheit_temp:.2f} °F")

    except ValueError:
        print("Please enter a valid temperature!")

if __name__ == "__main__":
    main()
