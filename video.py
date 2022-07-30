import cv2
from Vcompression import compress
from Vcolor import get_color
import os

vidcap = cv2.VideoCapture("test.mp4")
success, image = vidcap.read()
count = 0
while success:
    #LOOK INTO THREADING TO WAIT FOR EACH FRAME TO BE SCANNED CONSECUTIVELY
    filename = "/Users/sam/Programming/Image-processing/frames/frame%d.jpg" % count
    cv2.imwrite(filename, image)
    if count % 8 == 0:
        compress(filename)
        print(f"\nFrame {count}")
        rgb = get_color(filename)
    os.remove(filename)
    success, image = vidcap.read()
    count += 1
