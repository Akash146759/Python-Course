import tkinter as tk
from tkinter import messagebox

def convert_length():
    try:
        length = float(entry_length.get())
        if var_conversion.get() == "Meters to Kilometers":
            result = length / 1000
            label_result.config(text=f"{result} Kilometers")
        elif var_conversion.get() == "Kilometers to Meters":
            result = length * 1000
            label_result.config(text=f"{result} Meters")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Length Converter App")

# Input length
label_length = tk.Label(root, text="Enter Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Conversion options
var_conversion = tk.StringVar(value="Meters to Kilometers")
radio_m_to_km = tk.Radiobutton(root, text="Meters to Kilometers", variable=var_conversion, value="Meters to Kilometers")
radio_m_to_km.grid(row=1, column=0, padx=10, pady=5)
radio_km_to_m = tk.Radiobutton(root, text="Kilometers to Meters", variable=var_conversion, value="Kilometers to Meters")
radio_km_to_m.grid(row=1, column=1, padx=10, pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_length)
button_convert.grid(row=2, column=0, columnspan=2, pady=10)

# Result display
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
