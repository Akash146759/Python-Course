import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get the numbers from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        # Calculate the product
        product = num1 * num2
        # Display the result
        label_result.config(text=f"Product: {product}")
    except ValueError:
        # Show an error message if the input is not valid
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Multiplication App")

# Label and entry for the first number
label_num1 = tk.Label(root, text="Enter First Number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

# Label and entry for the second number
label_num2 = tk.Label(root, text="Enter Second Number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Button to calculate the product
button_calculate = tk.Button(root, text="Calculate Product", command=calculate_product)
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Product: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
