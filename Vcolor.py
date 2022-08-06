from PIL import Image
import cv2


def average(arr):
    """Gets average color for each r g and b value"""
    total = 0
    for value in arr:
        total += value
    return total // len(arr)


def get_color(image):

    img = cv2.imread(image)
    height = img.shape[0]
    width = img.shape[1]

    im = Image.open(image)
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
