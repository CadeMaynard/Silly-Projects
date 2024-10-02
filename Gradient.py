# Gradient
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
gradientInComplete = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill('white')
    # fill the screen with a color to wipe away anything from last frame
    if(gradientInComplete):
        for r in range(255):
            tempColor = pygame.Color(0,r,r)
            for theta in range(360):
                radTheta = math.radians(theta)
                x = MIDSCREEN + round(r * math.cos(radTheta),0)
                y = MIDSCREEN + round(r * math.sin(radTheta),0)
                tempRect = pygame.Rect((x,y),(4,4))
                pygame.draw.rect(screen, tempColor, tempRect)
                #pygame.display.update(tempRect)
            pygame.display.flip()
        gradientInComplete = False
    time.sleep(5)
    for r in range(255):
        tempColor = pygame.Color(0,255-r,255-r)
        pygame.draw.circle(screen, tempColor, (MIDSCREEN, MIDSCREEN), 255-r)
        pygame.display.flip()
    time.sleep(10)
    running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    #pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()