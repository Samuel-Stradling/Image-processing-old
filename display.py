import pygame
from color import get_color

pygame.init()


size = (900, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Average Color")

running = True

clock = pygame.time.Clock()
color = get_color("testImage.jpg")

# -------- Main Program Loop -----------
while running:
    pygame.display.update()
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)


pygame.quit()
