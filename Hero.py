from Creature import Creature
import pygame
from Img import *

vec = pygame.math.Vector2


class Hero(Creature):
    def __init__(self,name="Hero",hp=50,abbrv="@",Img=None,strength=2,inventory=None,gold=0):
        super().__init__(name,hp,abbrv,pygame.image.load("./Img/zelda_0.png"),strength)
        self._inventory=inventory
        self.gold=gold
        if self._inventory==None:
            self._inventory=[]
        self.gold=gold
        self.hp_max=50
        self.name=self.name
        self.map_pos = None
        self.strength=strength

    def description(self):
       return super().description()+str(self._inventory)

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
        
        
        