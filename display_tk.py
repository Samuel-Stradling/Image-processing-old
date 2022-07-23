from tkinter import *
from color import get_color

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

window = Tk()


size = "900x500"
window.geometry(size)
window.title("Average Color")


color = get_color("testImage.jpg")
window.config(background=_from_rgb(color))

window.mainloop()



