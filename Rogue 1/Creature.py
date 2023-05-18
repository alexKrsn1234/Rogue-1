from Element import Element
import pygame
from Img import *

vec = pygame.math.Vector2

class Creature(Element):
    monsters = {0: [("Goblin", 4), ("Bat", 2, "W")],
                1: [("Ork", 6, "", None, 2), ("Blob", 10)], 5: [("Dragon", 20, "", None, 3)]}
    
    def __init__(self,name,hp,abbrv="",Im=None,strength=-1):
        super().__init__(name,abbrv)
        self.hp=hp
        self.strength=strength
        if self.strength==-1:
            self.strength=1
        self.image = Im

    def description(self):
        return super().description()+"("+str(self.hp)+")"
    
    def meet(self,other):
        self.hp-=other.strength
        return  (self.hp<=0)

    @staticmethod
    def randMonster():
        return Element.randElement(Creature.monsters)
    
