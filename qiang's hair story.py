from math import *
import pygame 
from sys import exit
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,550),0,32)
pygame.display.set_caption("给光头强种头发")

grey = (230,230,230)
background = pygame.image.load("final.jpg").convert()
hair1 = pygame.image.load('hair.png')
hair=pygame.transform.scale(hair1,(100,100)).convert_alpha()     
while True:
    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos()
    x -= hair.get_width()/2
    y -= hair.get_height()/2
    screen.blit(hair,(x,y))
   
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            newhair = pygame.Rect(x,y,50,10)
            pygame.draw.arc(background,(0,0,0),newhair,0,pi/2,5)
    pygame.display.update()
