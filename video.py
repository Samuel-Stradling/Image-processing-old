import cv2
from Vcompression import compress
from Vcolor import get_color
import os
import pygame


def frame_color(frame):

    """Gets the color for each frame using the optimised get_color method from Vcolor"""

    filename = "/Users/sam/Programming/Image-processing/frames/frame.jpg"

    # saves the frame
    cv2.imwrite(filename, frame)
    # overwrites the file with the scaled down version of itself
    compress(filename)

    rgb = get_color(filename)
    # pygame fill the screen with the received average rgb
    screen.fill(rgb)
    # update the screen
    pygame.display.flip()
    # remove the saved frame
    os.remove(filename)


def play_video():

    """This plays all frames of the video (using cv2) and at fourth frame, gets the average color
    of the frame which is displayed with pygame.
    Scanning every frame is too slow so this does multiples [of 4]"""

    cap = cv2.VideoCapture(0) # video stream from hdmi is same as webcam

    # counter for the frames to allow for scanning of multiples of frames instead of each and every
    frameNo = 0

    while cap.isOpened():
        ret, frame = cap.read()

        frameNo += 1
        # if cap.read() is returning:
        if ret:
            # display that frame
            cv2.imshow("Video", frame)
            # 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            if frameNo % 4 == 0:
                print(frameNo)
                # time.sleep(1 / 60)
                frame_color(frame)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


# start of the actual code initing pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Average Color")
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # calls play_video which calls get_color when neccessary
    play_video()
