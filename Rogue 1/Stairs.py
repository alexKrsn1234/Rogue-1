from Element import Element
from Img import *
import pygame
from Hero import Hero

vec = pygame.math.Vector2

class Stairs(Element):
    stairsIm=pygame.image.load("./Img/escaliers.png")

    def __init__(self,name="Stairs",abbrv="E"):
        super().__init__(name,abbrv)
    
    def __repr__(self):
        return super().__repr__()
    
    def description(self):
        return super().description()
    
    def meet(self,other):
        if isinstance(other,Hero) :
            from Game import theGame
            from Map import Map
            theGame()._floor=Map(hero=Hero())
        
    def draw(self,c):
        screen.blit(self.starisIm, vec(c.x,c.y)*48)




