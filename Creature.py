from Element import Element
import pygame
from Img import *

vec = pygame.math.Vector2

class Creature(Element):
    Imgoblin=pygame.image.load("./Img/goblin.png")
    Imdemon=pygame.image.load("./Img/demon.png")
    Imbear=pygame.image.load("./Img/bear.png")
    Imshadow=pygame.image.load("./Img/shadow.png")
    monsters = {0: [("goblin", 4,"G"), ("demon", 2, "D")],
                1: [("bear", 6, "B", None, 2)], 5: [("shadow", 20, "S", None, 3)]}
    monsters_liste={"goblin": Imgoblin, "demon": Imdemon, "bear": Imbear, "shadow": Imshadow}
    
    def __init__(self,name,hp,abbrv="",Im=None,strength=-1, coord = None):
        super().__init__(name,coord, abbrv)
        self.hp=hp
        self.hp_max=self.hp
        self.strength=strength
        self.Im=Im
        if self.strength==-1:
            self.strength=1
        if self.name!="Hero" :
            self.Im=Creature.monsters_liste[self.name]
        self.rect=self.Im.get_rect()


    def description(self):
        return super().description()+"("+str(self.hp)+")"
    
    def meet(self,other):
        self.hp-=other.strength
        return  (self.hp<=0)

    @staticmethod
    def randMonster():
        return Element.randElement(Creature.monsters)
    
    def uptdate_health_bar(self,SCREEN):
        pygame.draw.rect(SCREEN, (111,210,46), pygame.Rect(self.rect.center,(self.hp/self.hp_max*48,8)))
    

    
