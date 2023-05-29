from Creature import Creature
import pygame
from Img import *

vec = pygame.math.Vector2


class Hero(Creature):
    def __init__(self,name="Hero",hp=50,abbrv="@",Img=None,strength=2,inventory=None,gold=0, xp=0):
        super().__init__(name,hp,abbrv,pygame.image.load("./Img/zelda_0.png"),strength)
        self._inventory=inventory
        self.gold=gold
        if self._inventory==None:
            self._inventory=[]
        self.gold=gold
        self.hp_max=50
        self.name=self.name
        self.strength=strength
        self.xp=xp
        self.xp_max=25
        self.levelxp=0

    def description(self):
       return super().description()+str(self._inventory)
    
    def modifxp(self):
        if self.xp>self.xp_max:
            self.xp=0
            self.levelxp+=1
            self.xp_max+=self.xp_max*2
            self.strength+=2
            self.hp=self.hp_max

    def take(self,e):
        if e.name=="gold":
            self.gold+=1   
        else :
            if len(self._inventory)<10 :
                return self._inventory.append(e)
            else :
                return self._inventory

    
    def use(self,item):
        if not (item in self._inventory):
            raise ValueError('Not in inventory')
        if item.use(self) :
            self._inventory.pop(self._inventory.index(item))

    def fullDescription(self):
        l=""
        for i in self.__dict__:
            l+=f"> {i[1:] if(i[0]=='_') else i} : {self.__dict__[i]}\n" if(i != "_inventory") else ""
        l+=f"> INVENTORY : {[i.name for i in self._inventory]}"
        return l
        
    def strInventory(self):
        l="> INVENTORY : \n"
        for i in self._inventory:
            l+=str(i.name)+"\n"
        return l
        
    def draw(self, SCREEN):
        super().draw(SCREEN)
        pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(630,25,200,20))
        pygame.draw.rect(SCREEN, (150,0,0), pygame.Rect(633,28,195,14))
        pygame.draw.rect(SCREEN, (111,210,46), pygame.Rect(633,28,self.hp/self.hp_max*195,14))
        
    def draw_xp(self,SCREEN):
        from Game import Game
        Game.draw_text(self,SCREEN,f"XP : {self.xp}/{self.xp_max}",Game.Font2,(255,255,255),500,45)
        Game.draw_text(self,SCREEN,f"Level : {self.levelxp}",Game.Font2,(255,255,255),480,60)
        pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(630,50,100,20))
        pygame.draw.rect(SCREEN, (150,150,150), pygame.Rect(633,53,95,14))
        pygame.draw.rect(SCREEN, (0,51,102), pygame.Rect(633,53,self.xp/self.xp_max*95,14))
