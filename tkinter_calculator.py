import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}", fg="green")
    except Exception as e:
        label_result.config(text="Error: Invalid Input", fg="red")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="lightgrey")

# Create a title label
label_title = tk.Label(root, text="Fancy Calculator", font=("Arial", 20), bg="lightgrey", fg="darkblue")
label_title.pack(pady=20)

# Create an entry widget for input
entry = tk.Entry(root, font=("Arial", 18), width=20, justify="center")
entry.pack(pady=20)

# Create buttons for operations
button_frame = tk.Frame(root, bg="lightgrey")
button_frame.pack(pady=10)

buttons = [
    ("1", lambda: entry.insert(tk.END, "1")),
    ("2", lambda: entry.insert(tk.END, "2")),
    ("3", lambda: entry.insert(tk.END, "3")),
    ("+", lambda: entry.insert(tk.END, "+")),
    ("4", lambda: entry.insert(tk.END, "4")),
    ("5", lambda: entry.insert(tk.END, "5")),
    ("6", lambda: entry.insert(tk.END, "-")),
    ("7", lambda: entry.insert(tk.END, "7")),
    ("8", lambda: entry.insert(tk.END, "8")),
    ("9", lambda: entry.insert(tk.END, "*")),
    ("0", lambda: entry.insert(tk.END, "0")),
    (".", lambda: entry.insert(tk.END, ".")),
    ("/", lambda: entry.insert(tk.END, "/")),
]

for i, (text, command) in enumerate(buttons):
    btn = tk.Button(button_frame, text=text, font=("Arial", 14), width=5, height=2, command=command)
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

# Create an equal button
btn_equal = tk.Button(root, text="=", font=("Arial", 14), bg="darkblue", fg="white", width=10, command=calculate)
btn_equal.pack(pady=20)

# Create a clear button
btn_clear = tk.Button(root, text="Clear", font=("Arial", 14), bg="red", fg="white", width=10, command=lambda: entry.delete(0, tk.END))
btn_clear.pack(pady=10)

# Create a result label
label_result = tk.Label(root, text="", font=("Arial", 16), bg="lightgrey", fg="black")
label_result.pack(pady=10)

# Run the application
root.mainloop()
