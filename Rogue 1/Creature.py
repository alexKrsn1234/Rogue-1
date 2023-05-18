from Element import Element
import pygame
from Img import *

vec = pygame.math.Vector2

class Creature(Element):
    
    def __init__(self,name,hp,abbrv="",Im=None,strength=-1):
        super().__init__(name,abbrv)
        self.hp=hp
        self.strength=strength
        if self.strength==-1:
            self.strength=1
        self.Im=pygame.image.load("./Img/"+str(self.name)+".png")
    def description(self):
        return super().description()+"("+str(self.hp)+")"
    
    def meet(self,other):
        from Game import theGame
        self.hp-=other.strength
        m="The "+other.name+" hits the "+self.description()
        theGame().addMessage(m)
        return  (self.hp<=0)

    def draw(self,x,y):
        from Game import theGame
        from main import screen
        theGame().screen.blit(self.Im, vec(x, y)*48)
