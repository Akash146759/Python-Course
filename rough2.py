from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Canvas Background")
root.geometry("400x300")

# Load the image
image = Image.open("background.jpg")  
bg_image = ImageTk.PhotoImage(image)

# Create a Canvas and add the image
canvas = Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")  # Position at top-left

root.mainloop()
