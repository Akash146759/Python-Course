import tkinter as tk
from PIL import Image, ImageDraw

# Initialize variables
drawing = False
start_x, start_y = None, None
mode = 'line'  # Default mode

# Create a blank canvas
canvas_size = (500, 500)
image = Image.new("RGB", canvas_size, (0, 0, 0))
draw = ImageDraw.Draw(image)

# Tkinter window setup
root = tk.Tk()
root.title("Annotated Image")

canvas = tk.Canvas(root, width=canvas_size[0], height=canvas_size[1], bg="black")
canvas.pack()

# Function for mouse events
def draw_shape(event):
    global start_x, start_y, drawing, mode

    if event.type == tk.EventType.ButtonPress:
        drawing = True
        start_x, start_y = event.x, event.y

    elif event.type == tk.EventType.Motion and drawing:
        canvas.delete("preview")
        if mode == 'line':
            canvas.create_line(start_x, start_y, event.x, event.y, fill="green", width=3, tags="preview")
        elif mode == 'rectangle':
            canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="blue", width=3, tags="preview")
        elif mode == 'circle':
            radius = int(((start_x - event.x) ** 2 + (start_y - event.y) ** 2) ** 0.5)
            canvas.create_oval(start_x - radius, start_y - radius, start_x + radius, start_y + radius, outline="yellow", width=3, tags="preview")

    elif event.type == tk.EventType.ButtonRelease:
        drawing = False
        if mode == 'line':
            draw.line([start_x, start_y, event.x, event.y], fill="green", width=3)
        elif mode == 'rectangle':
            draw.rectangle([start_x, start_y, event.x, event.y], outline="blue", width=3)
        elif mode == 'circle':
            radius = int(((start_x - event.x) ** 2 + (start_y - event.y) ** 2) ** 0.5)
            draw.ellipse([start_x - radius, start_y - radius, start_x + radius, start_y + radius], outline="yellow", width=3)

        # Update canvas with final drawing
        update_canvas()

# Function to update Tkinter canvas
def update_canvas():
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    canvas.image = tk_image

# Bind events
canvas.bind("<ButtonPress-1>", draw_shape)
canvas.bind("<Motion>", draw_shape)
canvas.bind("<ButtonRelease-1>", draw_shape)

# Run Tkinter loop
root.mainloop()

# Save final annotated image
image.save("annotated_output.png")
