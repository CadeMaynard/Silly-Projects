# Sin Float
# Cade Maynard
# 5-14-2024

# Example file showing a basic pygame "game loop"
import pygame
import math
import time

MIDSCREEN = 256
# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
i = 0
wColor = pygame.Color('white')

def f(x):
    y = (x/5) - 5
    y = -1 * (y*y) + 25
    if(y >= 0):
        return y
    else:
        return 0
    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    # fill the screen with a color to wipe away anything from last frame
    pointArr = [(50, 256 + 100*math.sin(math.radians(i))),
                (100, 256 + 100*math.sin(math.radians(i*2))),
                (150, 256 + 100*math.sin(math.radians(i*3))),
                (200, 256 + 100*math.sin(math.radians(i*4))),
                (250, 256 + 100*math.sin(math.radians(i))),
                (300, 256 + 100 * math.cos(math.radians(i*3))),
                (350, 256 + 5 * -f(i)),
                (400 + 100 * math.sin(math.radians(i)), 256 + 100*math.cos(math.radians(i)))]
    
    for point in pointArr:
        pygame.draw.circle(screen, wColor, point, 10)
    pygame.draw.lines(screen, 'blue', False, pointArr, 5)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    i +=1
    clock.tick(60)  # limits FPS to 60

pygame.quit()

