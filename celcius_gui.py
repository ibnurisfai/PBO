import tkinter as tk

def convert_temperature():
    try:
        celsius_temp = float(entry_celsius.get())
        kelvin_temp = celsius_temp + 273.15
        reamur_temp = celsius_temp * 0.8
        fahrenheit_temp = (celsius_temp * 9/5) + 32

        entry_kelvin.delete(0, tk.END)
        entry_kelvin.insert(0, f"{kelvin_temp:.2f}")

        entry_reamur.delete(0, tk.END)
        entry_reamur.insert(0, f"{reamur_temp:.2f}")

        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{fahrenheit_temp:.2f}")

    except ValueError:
        result_label.config(text="Please enter a valid temperature!")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Labels
label_celsius = tk.Label(root, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

label_kelvin = tk.Label(root, text="Kelvin:")
label_kelvin.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

label_reamur = tk.Label(root, text="Reamur:")
label_reamur.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, pady=10)

# Entry widgets
entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

entry_kelvin = tk.Entry(root)
entry_kelvin.grid(row=1, column=1, padx=10, pady=10)

entry_reamur = tk.Entry(root)
entry_reamur.grid(row=2, column=1, padx=10, pady=10)

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=3, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=4, column=0, columnspan=2)

# Run the main loop
root.mainloop()
