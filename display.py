import pygame
from color import averageRGB

pygame.init()


size = (900, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Average Color")

running = True

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while running:
    pygame.display.update()
    screen.fill(averageRGB)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(30)


pygame.quit()
