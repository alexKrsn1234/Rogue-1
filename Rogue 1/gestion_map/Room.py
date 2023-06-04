from autre.Coord import Coord
import random
import pygame
from elements_jeu.Creature import Creature
from elements_jeu.Equipment import Equipment


class Room (object):
    
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2
    
    def __repr__(self):
        return "["+str(self.c1) +", "+str(self.c2)+"]"
    
    def __contains__(self,coord):
        if self.c1.x<=coord.x<=self.c2.x :
            if self.c1.y<=coord.y<=self.c2.y :
                return True
    
    def center(self):
        return Coord(int(self.c1.x+self.c2.x)//2,int(self.c1.y+self.c2.y)//2)
    
    def intersect(self,room):
        
        coinHGA=(self.c1 in room)
        coinBDA=(self.c2 in room)
        coinBGA=(Coord(self.c1.x,self.c2.y) in room)
        coinHDA=(Coord(self.c2.x,self.c1.y) in room)
        
        coinHGB=(room.c1 in self)
        coinBDB=(room.c2 in self)
        coinBGB=(Coord(room.c1.x,room.c2.y) in self)
        coinHDB=(Coord(room.c2.x,room.c1.y) in self)
        
        if coinHGA or coinBDA or coinBGA or coinHDA or coinHGB or coinBDB or coinBGB or coinHDB :
            return True
        return False
    
    def randCoord(self):
        a=random.randint(self.c1.x,self.c2.x)
        b=random.randint(self.c1.y,self.c2.y)
        return Coord(a,b)
    
    def randEmptyCoord(self,map):
        c=self.randCoord()
        while (map.get(c) in map._elem) or (c==self.center()) :
            c=self.randCoord()
        return c
    
    def decorate(self,map):

        c1=self.randEmptyCoord(map)
        map.put(c1,Equipment(*Equipment.randEquipment(), coord=c1))
        print(Equipment.randEquipment())
        c1=self.randEmptyCoord(map)
        map.put(c1,Creature(*Creature.randMonster(), coord=c1))
    
