from PIL import Image


def compress(directory):

    """resizes the given image and saves as C_image.jpg. Returns the new directory"""

    # set the base width of the image
    widthRescale = 300
    img = Image.open(directory)
    # determining the height ratio to maintain the aspect ratio
    wpercent = widthRescale / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    # resize image and save
    img = img.resize((widthRescale, hsize), Image.Resampling.LANCZOS)
    # find index of final occurence of slash
    lastslash = directory.rfind("/") + 1

    # saves the compressed file preceded by C
    directory = list(directory)
    directory.insert(lastslash, "C")
    directory = "".join(directory)
    img.save(directory)
    return directory



