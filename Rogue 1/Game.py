from Coord import Coord
from Hero import Hero
from Creature import Creature
from Element import Element
from Room import Room
from Equipment import Equipment
from Stairs import Stairs
import random
from Map import Map
from Element import Element
from Equipment import Equipment 
import copy
from getch import getch
import pygame 

def heal(creature):
    creature.hp+=3
    return True

def teleport(creature, unique):
    theGame()._floor.rm(theGame()._floor.pos(creature))
    r=random.choice(theGame()._floor._rooms)
    c=r.randEmptyCoord(theGame()._floor)
    theGame()._floor.put(c,creature)
    return unique

#Init :
pygame.init()

#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("Sword.png")
pygame.display.set_icon(icon)

#Screen :
screen=pygame.display.set_mode((800,600))

class Game(object):
    
    equipments = { 0: [ Equipment("potion","!",lambda h : heal(h)), Equipment("gold","o") ], 1: [ Equipment("sword"), Equipment("bow"),Equipment("potion","!",lambda h : teleport(h,True)) ], 2: [ Equipment("chainmail") ], 3: [Equipment("portoloin","w",lambda h : teleport(h,False))] }
    monsters = { 0: [ Creature("Goblin",4), Creature("Bat",2,"W") ], 1: [ Creature("Ork",6,strength=2), Creature("Blob",10) ], 5: [ Creature("Dragon",20,strength=3) ] }
    _actions={'z': lambda h : theGame()._floor.move(h,Coord(0,-1)), 's': lambda h : theGame()._floor.move(h,Coord(0,1)), 'd': lambda h : theGame()._floor.move(h,Coord(1,0)), 'q': lambda h: theGame()._floor.move(h,Coord(-1,0)),'i' : lambda h : theGame().addMessage(h.fullDescription()),'k' : lambda h : h.__setattr__("_hp",0), ' ' : lambda h : theGame(),'u' : lambda h : h.use(theGame().select(h._inventory))  }
    
    
    def __init__(self,hero=None,level=1,floor=None,message=None):
        self.hero=hero
        if self.hero==None:
            self.hero=Hero()
        self._level=level
        self._hero=self.hero
        self._floor=floor
        self._message=message
        if self._message==None :
            self._message=[]

    def buildFloor(self):
        self._floor=Map(hero=self._hero)
        self._floor.put(Room.center(self._floor._rooms[-1]),Stairs())
    
    def addMessage(self,m):
        self._message.append(m)
    
    def readMessages(self):
        totm=""
        for i in range(len(self._message)) :
            totm+=self._message[i]+". "
        self._message=[]
        return totm
    
    def randElement(self, collection):
        X=random.expovariate(1/self._level)
        for x in collection :
            if x<X :
                indice=x
        l=random.choice(collection[indice])
        lc=copy.copy(l)
        return lc
        
    def randEquipment(self):
        return self.randElement(self.equipments)
    
    def randMonster(self):
        return self.randElement(self.monsters)
        
    def select(self,liste):
         l=[str(liste.index(x))+": "+x.name for x in liste]
         print("Choose item> "+str(l))
         n=getch()
         if n.isdigit() and int(n)<=len(l) :
             return liste[int(n)]

    def play(self):
        """Main game loop"""
        self.buildFloor()
        print("--- Welcome Hero! ---")
        while self.hero.hp > 0:
            print()
            print(self._floor)
            print(self.hero.description())
            print(self.readMessages())
            c = getch()
            if str(c)[2] in Game._actions:
                Game._actions[str(c)[2]](self.hero)
            self._floor.moveAllMonsters()
        print("--- Game Over ---")
    
def theGame(game=Game()) :
    return game


theGame().play()


                
