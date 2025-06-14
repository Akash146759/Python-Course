from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("Multi-File Text Editor")
window.geometry("800x600")

# Create Notebook for Tabs
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

open_files = {}  # Dictionary to track opened files

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath or filepath in open_files:
        return

    # Create new tab
    frame = Frame(notebook)
    txt_edit = Text(frame)
    txt_edit.pack(expand=True, fill="both")
    
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)

    notebook.add(frame, text=filepath.split("/")[-1])  # Show filename in tab
    open_files[filepath] = txt_edit  # Track opened file

def save_file():
    """Save the currently active file."""
    current_tab = notebook.select()  # Get current tab ID
    if not current_tab:
        return
    
    index = notebook.index(current_tab)
    filepath = list(open_files.keys())[index]  # Get associated filepath
    txt_edit = open_files[filepath]  # Get associated Text widget
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)

def save_as_file():
    """Save the content to a new file."""
    current_tab = notebook.select()
    if not current_tab:
        return

    filepath = asksaveasfilename(defaultextension="txt",
                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return

    index = notebook.index(current_tab)
    txt_edit = list(open_files.values())[index]
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)

    # Update tab name & tracking dictionary
    notebook.tab(current_tab, text=filepath.split("/")[-1])
    open_files[filepath] = txt_edit

# Create Frame for Buttons
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save", command=save_file)
btn_save_as = Button(fr_buttons, text="Save As...", command=save_as_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.pack(side="left", fill="y")

window.mainloop()
