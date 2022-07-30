import cv2
from color import get_color

vidcap = cv2.VideoCapture("test.mp4")
success, image = vidcap.read()
count = 0
while success:
    #LOOK INTO THREADING TO WAIT FOR EACH FRAME TO BE SCANNED CONSECUTIVELY
    # change to save to /frames ("PATH/frame%d.jpg")
    cv2.imwrite("/Users/sam/Programming/Image-processing/frames/frame%d.jpg" % count, image)
    get_color("/Users/sam/Programming/Image-processing/frames/frame%d.jpg" % count)
    success, image = vidcap.read()
    print("Read a new frame: ", success)
    count += 1
