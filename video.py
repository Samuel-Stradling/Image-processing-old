import cv2
from Vcompression import compress
from Vcolor import get_color
import os
import pygame
import time

#LOOK INTO THREADING TO CONTROL SPEED OF ANALYSIS
def video_color():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Avg Color")
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        clock.tick(60)

        vidcap = cv2.VideoCapture("test2.mp4")
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
                screen.fill(rgb)
                pygame.display.flip()

            os.remove(filename)
            success, image = vidcap.read()
            count += 1
            if count == 0:
                success = False
                break
        if success == False:
            time.sleep(5)
            break
        

    pygame.quit()
video_color()