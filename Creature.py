from Element import Element
import pygame
from Img import *

vec = pygame.math.Vector2

class Creature(Element):
    Imgoblin=pygame.image.load("./Img/goblin.png")
    Imdemon=pygame.image.load("./Img/demon.png")
    Imbear=pygame.image.load("./Img/bear.png")
    Imshadow=pygame.image.load("./Img/shadow.png")
    monsters = {0: [("goblin", 4,"G"), ("demon", 3, "D")],
                1: [("bear", 6, "B", None, 2)], 5: [("shadow", 20, "S", None, 3)]}
    monsters_liste={"goblin": Imgoblin, "demon": Imdemon, "bear": Imbear, "shadow": Imshadow}
    monsters_liste_xp= {"goblin": 5, "demon": 2, "bear": 7, "shadow": 10}

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
            self.xp=Creature.monsters_liste_xp[self.name]

    def description(self):
        return super().description()+"("+str(self.hp)+")"
    
    def meet(self,other):
        self.hp-=other.strength
        if other.name=="Hero" and self.hp<=0:
            other.xp+=self.xp
            other.modifxp()
        return  (self.hp<=0)

    @staticmethod
    def randMonster():
        return Element.randElement(Creature.monsters)
    
    def draw(self, SCREEN):
        from Game import theGame
        super().draw(SCREEN)
        if self.name=="demon" :
            if  theGame()._floor.pos(self).distance(theGame()._floor.pos(theGame()._floor.hero))==1:
                pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(self.coord.x*48-1,self.coord.y*48-8,50,10))
                pygame.draw.rect(SCREEN, (150,0,0), pygame.Rect(self.coord.x*48,self.coord.y*48-7,48,8))
                pygame.draw.rect(SCREEN, (111,210,46), pygame.Rect(self.coord.x*48,self.coord.y*48-7,self.hp/self.hp_max*48,8))
            else :
                pass
        else :
            pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(self.coord.x*48-1,self.coord.y*48-8,50,10))
            pygame.draw.rect(SCREEN, (150,0,0), pygame.Rect(self.coord.x*48,self.coord.y*48-7,48,8))
            pygame.draw.rect(SCREEN, (111,210,46), pygame.Rect(self.coord.x*48,self.coord.y*48-7,self.hp/self.hp_max*48,8))
    
