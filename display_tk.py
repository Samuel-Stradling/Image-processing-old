from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from color import get_color


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code"""
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


window = Tk()


size = "900x500"
window.geometry(size)
window.title("Average Color")


def select_file():
    filetypes = (("image files", "*.jpg"), ("All files", "*.*"), ("image files", "*.png"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="/", filetypes=filetypes
    )
    get_change_color(filename)
    #print(f"\n{filename}\n")


def get_change_color(directory):
    color = get_color(directory)
    textLabel.pack_forget()
    open_button.pack_forget()
    window.config(background=_from_rgb(color))


global textLabel
textLabel = Label(
    window, text="Find the average color of an image", font=("Arial", 25, "bold")
)
textLabel.pack(pady=15)

global open_button
open_button = ttk.Button(window, width=35, text="Open a File", command=select_file)
# open_button.configure(command=lambda: get_change_color(textLabel, open_button))
open_button.pack()


window.mainloop()
