import sys
import pygame
import math
import numpy as np

pygame.init()

#colous
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (250,230,50)
cyan = (0,220,220)
magenta = (255,0,255)

#initialize window 
WIDTH = 1000
HIEGHT = 1000

screen = pygame.display.set_mode((WIDTH, HIEGHT))
title = "2d rotation test"
pygame.display.set_caption(title)

clock = pygame.time.Clock()

frameRate = 60




def rotatePoint(point, angle):
    cos0 = math.cos(angle)
    sin0 = math.sin(angle)

    x = point[0]
    y = point[1]

    rotmat = np.array([[cos0, -sin0],
                       [sin0, cos0]])
    
    v = np.array([x,y])

    rotated = np.matmul(rotmat, v)

    posx = rotated[0]
    posy = rotated[1]

    return (posx,posy)
    



def drawPoints(points):
    for point in points:
        x = point[0] + WIDTH/2
        y = point[1] + HIEGHT/2

        pygame.draw.circle(screen,white,(x,y),5)
    


points = [(100,100),(200,50),(-80, 0)]

while True:
#INPUT DETECTION
    for event in pygame.event.get():
        #close window
        if event.type == pygame.QUIT:
            sys.exit()
        
    screen.fill(black)

    drawPoints(points)


    points[0] = rotatePoint(points[0],math.pi/50)

    points[1] = rotatePoint(points[1],math.pi/150)

    points[2] = rotatePoint(points[2],math.pi/100)

    
    clock.tick(frameRate)
    pygame.display.update()