from PIL import Image
def compress(directory):
    # set the base width of the result
    widthRescale = 300 #change to control rescaling of image
    img = Image.open(directory)
    # determining the height ratio
    wpercent = (widthRescale/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    # resize image and save
    img = img.resize((widthRescale,hsize), Image.Resampling.LANCZOS)
    img.save(directory)
#compress("/Users/sam/Pictures/mac tonight/2.jpg")