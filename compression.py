from PIL import Image
def compress(directory):
    # set the base width of the result
    basewidth = 300
    img = Image.open(directory)
    # determining the height ratio
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    # resize image and save
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    lastslash = directory.rfind("/") + 1
    directory = list(directory)
    directory.insert(lastslash, "C")
    directory = ''.join(directory)
    img.save(directory)
compress("/Users/sam/Pictures/mac tonight/2.jpg")