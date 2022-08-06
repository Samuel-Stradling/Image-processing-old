from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from color import get_color
from compression import compress
import os


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code"""
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


window = Tk()


size = "900x500"
window.geometry(size)
window.title("Average Color")


def select_file():
    """Selects file using tkinter gui"""
    filetypes = (("image files", "*.jpg"), ("All files", "*.*"), ("image files", "*.png"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="/", filetypes=filetypes
    )

    filename = compress(filename) 
    get_change_color(filename)
    


def get_change_color(directory):
    """Gets rid of the labels and updates background color"""
    color = get_color(directory)
    textLabel.pack_forget()
    open_button.pack_forget()
    window.config(background=_from_rgb(color))
    os.remove(directory)



global textLabel
textLabel = Label(
    window, text="Find the average color of an image", font=("Arial", 25, "bold")
)
textLabel.pack(pady=15)

global open_button
open_button = ttk.Button(window, width=35, text="Open a File", command=select_file)
#can only have one function for command, so select_file hosts change color
open_button.pack()


window.mainloop()
