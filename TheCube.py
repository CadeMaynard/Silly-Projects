# The Cube
# No mortal man can comprehend his ways
# Cade Maynard
# 9-13-2024

import pygame
import math
from copy import deepcopy

MIDSCREEN = 300
# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

def scalMult(c, a):
    v = len(a) * [0]
    for i in range(len(a)):
        v[i] = c*a[i]
    return v

def vecAdd(a,b):
    if(len(a) == len(b)):
        v = len(a)*[0]
        for i in range(len(a)):
            v[i] = a[i] + b[i]
        return v
    else:
        return -1

def dot(a,b):
    return (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])

def cross(a,b):
    return [(a[1]*b[2]) - (a[2]*b[1]), (a[2]*b[0]) - (a[0]*b[2]), (a[0]*b[1]) - (a[1]*b[0])]

def rodRot(v, k, theta):
    cos = math.cos(theta)
    return vecAdd(vecAdd(scalMult(cos, v), scalMult(math.sin(theta), cross(k,v))), scalMult(dot(k, v) * (1 - cos), k))

class Cube:
    def __init__(self, angleRot=0, size=150, x=MIDSCREEN,y=MIDSCREEN): # surfaces in the following form [[(x_0,y_0,z_0), (x_1,y_1,z_1), (x_2,y_2,z_2)],[...]]
        rotRad = math.radians(angleRot + 90)
        self.rotVec = [math.cos(rotRad),math.sin(rotRad), 0]
        self.sinMult = size * .2
        sizeHalf = size/2
        xyz =[[sizeHalf,sizeHalf,sizeHalf],[sizeHalf,-sizeHalf,sizeHalf],[-sizeHalf,-sizeHalf,sizeHalf],[-sizeHalf,sizeHalf,sizeHalf],
            [sizeHalf,sizeHalf,-sizeHalf],[sizeHalf,-sizeHalf,-sizeHalf],[-sizeHalf,-sizeHalf,-sizeHalf],[-sizeHalf,sizeHalf,-sizeHalf]]
        surfaces =[xyz[:4],
                [xyz[0],xyz[3],xyz[7],xyz[4]],
                [xyz[0],xyz[1],xyz[5],xyz[4]],
                [xyz[1],xyz[2],xyz[6],xyz[5]],
                [xyz[2],xyz[3],xyz[7],xyz[6]],
                xyz[4:]]

        _, screenY = pygame.display.get_window_size()
        self.x,self.y = x, screenY - y
        colors = ['red', 'blue', 'green','yellow','purple','teal']
        self.surfaces = [0]*len(surfaces)
        self.i = 0
        for i in range(len(surfaces)):
            self.surfaces[i] = {"color":pygame.Color(colors[i]),
                                "points":deepcopy(surfaces[i]),
                                "height":0,
                                "zAvg": 0}
            for n in self.surfaces[i]["points"]:
                self.surfaces[i]["zAvg"] += n[2]
            self.surfaces[i]["zAvg"] = self.surfaces[i]["zAvg"]/len(self.surfaces[i]["points"])

    def calcPoints(self):
        self.i += 1
        for surface in self.surfaces:
            #surface.movePoints(self.rotVec, 1)
            for i in range(len(surface["points"])):
                surface["points"][i] = rodRot(surface["points"][i], self.rotVec, math.radians(1))
            surface["zAvg"] = 0
            for n in surface["points"]:
                surface["zAvg"] += n[2]
            surface["zAvg"] = surface["zAvg"]/len(surface["points"])
            surface["height"] = math.sin(math.radians(self.i*1.5)) * self.sinMult

    def render(self):
        for surface in self.surfaces:
            if(surface["zAvg"] > 0):
                pygame.draw.polygon(screen, surface["color"], list(map(lambda point: [point[0] + self.x, point[1] + self.y + surface["height"]], surface["points"])))
                #surface.render()

cubes = [0]*36
i = 0
#for i in range(360):
while(i < 360):
    cubes[int(i/10)] = Cube(i, 40, MIDSCREEN + math.sin(math.radians(i))*100, MIDSCREEN + math.cos(math.radians(i))*100)
    i+=10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    # fill the screen with a color to wipe away anything from last frame
    
    # RENDER YOUR GAME HERE
    for cube in cubes:    
        cube.calcPoints()
        cube.render()

    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()

