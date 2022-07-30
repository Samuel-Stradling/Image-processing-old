import cv2
from compression import compress
from colorForVideo import get_color
import os

vidcap = cv2.VideoCapture("test.mp4")
success, image = vidcap.read()
count = 0
while success:
    #LOOK INTO THREADING TO WAIT FOR EACH FRAME TO BE SCANNED CONSECUTIVELY
    # change to save to /frames ("PATH/frame%d.jpg")
    cv2.imwrite("/Users/sam/Programming/Image-processing/frames/frame%d.jpg" % count, image)
    filename = compress("/Users/sam/Programming/Image-processing/frames/frame%d.jpg" % count)
    rgb = get_color(filename)
    os.remove(filename)
    os.remove("/Users/sam/Programming/Image-processing/frames/frame%d.jpg" % count)
    success, image = vidcap.read()
    count += 1
