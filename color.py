# from statistics import mode
from PIL import Image
import cv2
import time


def average(arr):

    """Gets average color for each r g and b value"""

    total = 0
    for value in arr:
        total += value
    return total // len(arr)


def get_color(image):

    """gets the mean color of the given parameter image. Creates a list of r, g, and b values respectively
    and gets the mean value for each of the lists. The process time is recorded and printed and the rgb
    value is returned as a tuple"""

    # starts a timer to record the process time taken
    t1_start = time.time()

    img = cv2.imread(image)
    height = img.shape[0]
    width = img.shape[1]
    # dimensions = (width, height)
    # print(dimensions)

    im = Image.open(image)
    # converts the given hex values for the image into rgb using a method from PIL
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

    t1_stop = time.time()
    # to get MEAN
    averageRGB = (average(rValues), average(gValues), average(bValues))
    # averageRGB = (mode(rValues), mode(gValues), mode(bValues)) #to get MODE
    processTime = abs(t1_start - t1_stop)
    print(processTime)
    print(averageRGB)
    return averageRGB
