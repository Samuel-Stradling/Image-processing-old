import cv2
from Vcompression import compress
from Vcolor import get_color
import os
import pygame
import time


def frame_color(frame):
    filename = "/Users/sam/Programming/Image-processing/frames/frame.jpg"
    cv2.imwrite(filename, frame)

    compress(filename)
    rgb = get_color(filename)
    screen.fill(rgb)
    pygame.display.flip()

    os.remove(filename)


def play_video():
    cap = cv2.VideoCapture("test2.mp4")
    frameNo = 0
    while cap.isOpened():
        ret, frame = cap.read()

        frameNo += 1
        if ret:
            cv2.imshow("frame", frame)
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


pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Avg Color")
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    play_video()
