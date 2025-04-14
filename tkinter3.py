import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Example Tkinter Window")
root.geometry("400x300")

# Create a top frame
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x")

# Create a bottom frame
bottom_frame = tk.Frame(root, bg="lightgreen", height=200)
bottom_frame.pack(fill="both", expand=True)

# Add a label to the top frame
top_label = tk.Label(top_frame, text="Welcome to Tkinter!", font=("Arial", 14))
top_label.pack(pady=20)

# Add buttons to the bottom frame
button1 = tk.Button(bottom_frame, text="Button 1", command=lambda: print("Button 1 clicked"))
button1.pack(side="left", padx=20, pady=20)

button2 = tk.Button(bottom_frame, text="Button 2", command=lambda: print("Button 2 clicked"))
button2.pack(side="left", padx=20, pady=20)

# Run the application
root.mainloop()
