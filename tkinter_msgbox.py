from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found. Do not close this window!")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=100, y=120)

# Entering main event loop
root.mainloop()