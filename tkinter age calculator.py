import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_age():
    try:
        # Get the input date
        birth_date = datetime.strptime(entry_date.get(), "%Y-%m-%d")
        current_date = datetime.now()
        
        # Calculate age
        age_years = current_date.year - birth_date.year
        age_months = current_date.month - birth_date.month
        age_days = current_date.day - birth_date.day

        # Adjust for negative values in months or days
        if age_days < 0:
            age_months -= 1
            age_days += (birth_date + timedelta(days=30)).day
        if age_months < 0:
            age_years -= 1
            age_months += 12
        
        label_result.config(text=f"Your age is {age_years} years, {age_months} months, and {age_days} days.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in the format YYYY-MM-DD!")

# Create the main window
root = tk.Tk()
root.title("Age Calculator App")

# Input label
label_date = tk.Label(root, text="Enter Your Birthdate (YYYY-MM-DD):")
label_date.grid(row=0, column=0, padx=10, pady=10)

# Input field
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.grid(row=1, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
