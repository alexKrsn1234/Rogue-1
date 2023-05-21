from Element import Element
import pygame
from Img import *

vec = pygame.math.Vector2

Imgoblin=pygame.image.load("./Img/goblin.png")
Imdemon=pygame.image.load("./Img/demon.png")
Imbear=pygame.image.load("./Img/bear.png")
Imshadow=pygame.image.load("./Img/shadow.png")

class Creature(Element):
    monsters = {0: [("goblin", 4,"G"), ("demon", 2, "D")],
                1: [("bear", 6, "B", None, 2)], 5: [("shadow", 20, "S", None, 3)]}
    
    def __init__(self,name,hp,abbrv="",Im=None,strength=-1, coord = None):
        super().__init__(name,coord, abbrv)
        self.hp=hp
        self.strength=strength
        if self.strength==-1:
            self.strength=1
        if self.name=="goblin":
            self.Im=Imgoblin
        elif self.name=="demon":
            self.Im=Imdemon
        elif self.name=="bear":
            self.Im=Imbear
        elif self.name=="shadow":
            self.Im=Imshadow

    def description(self):
        return super().description()+"("+str(self.hp)+")"
    
    def meet(self,other):
        self.hp-=other.strength
        return  (self.hp<=0)

    @staticmethod
    def randMonster():
        return Element.randElement(Creature.monsters)
    

    
