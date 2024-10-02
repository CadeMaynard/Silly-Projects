import pygame
import math

JUMP_MULT = 10
MOVE_MULT = .8
BOX_DIM = (25, 45)

class pc:
    def __init__(self, initialX, initialY):
        self.x = initialX
        self.y = initialY
        self.coord = (self.x, self.y)
        self.box = pygame.Rect(self.coord, BOX_DIM)
        self.xIncre = 0
        self.yIncre = -1

    def jump(self, x):
        y = (x/5) - 5
        y = 2 * y
        y = -1 * (y/5)
        if(x >= 0 and x <= 50):
            self.yIncre += 1
            return y * JUMP_MULT
        else:
            return 0
        
    def walk(self, x):
        if(x > 0):
            self.xIncre += 1
            return (math.log(x) + 2) * MOVE_MULT
        elif(x < 0):
            self.xIncre -= 1
            return (-1 * (math.log(-1*x) + 2)) * MOVE_MULT
        else:
            return 0

    def input(self, inputs):
        if(inputs.key == pygame.K_a or inputs.key == pygame.K_d):
            if(inputs.key == pygame.K_a):
                self.xIncre =-1 * (inputs.type == pygame.KEYDOWN)
            elif(inputs.key == pygame.K_d):
                self.xIncre = inputs.type == pygame.KEYDOWN
        elif(inputs.key == pygame.K_SPACE and inputs.type == pygame.KEYDOWN):
            self.yIncre = 0
        # print("Going straight horse mode over here")

    def refresh(self):
        self.x += self.walk(self.xIncre)
        self.y -= self.jump(self.yIncre)
        self.box.update((self.x,self.y), BOX_DIM)

        '''
        The idea of this function is that it will run the calculations of the above inputs
        on a frame by frame basis.
        '''
