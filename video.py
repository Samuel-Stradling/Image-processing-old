import cv2
from color import get_color

vidcap = cv2.VideoCapture("test.mp4")
success, image = vidcap.read()
count = 0
while success:
    # change to save to /frames ("PATH/frame%d.jpg")
    cv2.imwrite("frame%d.jpg" % count, image)
    success, image = vidcap.read()
    print("Read a new frame: ", success)
    count += 1
