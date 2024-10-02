# Sin Float
# Cade Maynard
# 5-14-2024

# Example file showing a basic pygame "game loop"
import pygame
import math
import time
from playerCharacter import pc

MIDSCREEN = 256
# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
i = 0
color = pygame.Color('white')

bilbo = pc(256, 400)
screen.fill('black')
while running:

    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            bilbo.input(event)
    screen.fill('black')
    # fill the screen with a color to wipe away anything from last frame
    
    
    '''for point in pointArr:
        pygame.draw.circle(screen, wColor, point, 10)
    pygame.draw.lines(screen, 'blue', False, pointArr, 5)'''

    # RENDER YOUR GAME HERE
    '''
    if(i%30 < 15):
        color = pygame.Color('blue')
    else:
        color = pygame.Color('white')
    '''
    bilbo.refresh()
    pygame.draw.rect(screen, color, bilbo.box)
    # flip() the display to put your work on screen
    pygame.display.flip()
    i +=1
    clock.tick(60)  # limits FPS to 60

pygame.quit()

