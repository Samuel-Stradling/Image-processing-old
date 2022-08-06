from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from color import get_color
from compression import compress
import os


def _from_rgb(rgb):

    """translates an rgb tuple of int to a tkinter friendly color code (HEX)"""

    r, g, b = rgb

    return f"#{r:02x}{g:02x}{b:02x}"


# initialising tkinter window
window = Tk()
size = "900x500"
window.geometry(size)
window.title("Average Color")


def select_file():

    """Selects file using tkinter gui"""

    filetypes = (
        ("image files", "*.jpg"),
        ("All files", "*.*"),
        ("image files", "*.png"),
    )

    # starts a file open dialog
    filename = fd.askopenfilename(
        title="Open a file", initialdir="/", filetypes=filetypes
    )

    filename = compress(filename)
    get_change_color(filename)


def get_change_color(directory):

    """calls the get_color function with the selected image.
    Also removes the widgets in order to display the new background color with
    a plain background. Is a chain of functions becuase the button action can only accept one method as
    the command"""

    color = get_color(directory)
    textLabel.pack_forget()
    open_button.pack_forget()
    window.config(background=_from_rgb(color))
    os.remove(directory)


# widgets made global to reduce bloating the functions with extra parameters
global textLabel
textLabel = Label(
    window, text="Find the average color of an image", font=("Arial", 25, "bold")
)
textLabel.pack(pady=15)

global open_button
open_button = ttk.Button(window, width=35, text="Open a File", command=select_file)
# can only have one function for command, so select_file hosts change color
open_button.pack()


window.mainloop()
