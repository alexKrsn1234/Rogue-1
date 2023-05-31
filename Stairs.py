from Element import Element
from Img import *
import pygame
from Hero import Hero

vec = pygame.math.Vector2

class Stairs(Element):
    stairsIm=pygame.image.load("./Img/escaliers.png")

    def __init__(self,name="Stairs",coord=None,abbrv="E"):
        super().__init__(name,coord,abbrv)
        self.Im = Stairs.stairsIm
    
    def __repr__(self):
        return super().__repr__()
    
    def description(self):
        return super().description()
    
    def meet(self,other):
        if isinstance(other,Hero) :
            from Game import theGame
            from Map import Map
            theGame()._floor=Map(size=int(theGame().Modulo),hero = theGame()._floor.hero)
            theGame()._floor.hero.repos=True
            theGame().buildFloor(theGame()._floor)
        




