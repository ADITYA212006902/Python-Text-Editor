# import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox

# Main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Global file path
file_path = None

# Create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 18)
)
text.pack(expand=True, fill=tk.BOTH)

# Function 1 - New File
def new_file():
    global file_path
    text.delete(1.0, tk.END)
    file_path = None

# Function 2 - Open File
def open_file():
    global file_path
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Function 3 - Save File
def save_file():
    global file_path
    if not file_path:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully")

# Create Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run application
root.mainloop()