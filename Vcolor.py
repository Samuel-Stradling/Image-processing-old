from PIL import Image
import cv2


def average(arr):
    """Gets average color for each r g and b value"""
    total = 0
    for value in arr:
        total += value
    return total // len(arr)


def get_color(image):

    """OPTIMISED FOR VIDEO. Gets the mean color of the given parameter image. Creates a list of r, g, and b values respectively
    and gets the mean value for each of the lists. The process time is recorded and printed and the rgb
    value is returned as a tuple"""

    img = cv2.imread(image)
    height = img.shape[0]
    width = img.shape[1]

    im = Image.open(image)
    # converts the given hex values for the image into rgb using a method from PIL
    rgb_im = im.convert("RGB")
    rValues = []
    gValues = []
    bValues = []
    for horElem in range(width - 1):
        for verElem in range(height - 1):
            r, g, b = rgb_im.getpixel((horElem, verElem))
            rValues.append(r)
            gValues.append(g)
            bValues.append(b)

    averageRGB = (average(rValues), average(gValues), average(bValues))  # to get MEAN
    # averageRGB = (mode(rValues), mode(gValues), mode(bValues)) #to get MODE
    print(averageRGB)
    return averageRGB
