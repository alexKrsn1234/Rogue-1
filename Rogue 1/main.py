import pygame

#Init :
pygame.init()

#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Screen :
screen=pygame.display.set_mode((800,600))