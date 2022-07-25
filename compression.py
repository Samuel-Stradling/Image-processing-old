#compress an image, save it, then access and get the color of the compressed image
#delete the compressed image after use
import PIL
import os
import glob
from PIL import Image
def compress(filename):
    img = Image.open(filename)
    img.save("Compressed_"+filename, optimize=True, quality=30)
    return "Compressed_"+filename
    #the compressed string is being appended to the whole path, instead of the filename
