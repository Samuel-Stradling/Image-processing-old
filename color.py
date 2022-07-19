from statistics import mode
from PIL import Image
import cv2

img = cv2.imread("testImage.jpg")
height = img.shape[0]
width = img.shape[1]

print(f"height: {height} \nwidth: {width}")

im = Image.open("testImage.jpg")
rgb_im = im.convert("RGB")
colors = []
for horElem in range(width - 1):
    for verElem in range(height - 1):
        r, g, b = rgb_im.getpixel((horElem, verElem))
        colors.append([r, g, b])

rValues = []
gValues = []
bValues = []
for rgb in colors:
    rValues.append(rgb[0])
    gValues.append(rgb[1])
    bValues.append(rgb[2])

print(mode(rValues))
print(mode(gValues))
print(mode(bValues))
