from statistics import mode
from PIL import Image
import cv2
import time


def get_color(image):
    t1_start = time.process_time()

    img = cv2.imread(image)
    height = img.shape[0]
    width = img.shape[1]

    im = Image.open(image)
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

    t1_stop = time.process_time()
    processTime = t1_stop - t1_start
    print(processTime)
    averageRGB = (mode(rValues), mode(gValues), mode(bValues))
    print(averageRGB)
    return averageRGB
