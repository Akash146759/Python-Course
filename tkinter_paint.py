import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("800x600")

        self.color = "black"  # Default color
        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=500)
        self.canvas.pack(pady=20)

        self.canvas.bind("<B1-Motion>", self.paint)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        self.color_btn = tk.Button(btn_frame, text="Choose Color", command=self.choose_color)
        self.color_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear_canvas)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Color")[1]
        if color_code:
            self.color = color_code

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
