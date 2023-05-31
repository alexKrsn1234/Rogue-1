from Coord import Coord
from Hero import Hero
from Creature import Creature
from Element import Element
from Equipment import Equipment
from Room import Room
from Stairs import Stairs
import random
import pygame
import time

#Init :
pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load(r'audio\Menu_Music.mp3')
#pygame.mixer.music.play(-1)
#   pygame.mixer.music.set_volume(1.0)
vec = pygame.math.Vector2
#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("./Img/icon.png")
pygame.display.set_icon(icon)

#Screen :



class Map:
    groundIm=pygame.image.load("./Img/sol1.png")
    ground="."
    emptyIm=pygame.image.load("./Img/mur1.png")
    empty=" "
    direction = {pygame.K_z:vec(0,-1) , pygame.K_d:vec(1,0), pygame.K_q:vec(-1,0), pygame.K_s:vec(0,1)}
    heroImg0=pygame.image.load("./Img/zelda_0.png")
    stairsIm=pygame.image.load("./Img/escaliers.png")
    dir={pygame.K_z: Coord(0,-1), pygame.K_s: Coord(0,1), pygame.K_d: Coord(1,0), pygame.K_q: Coord(-1,0)}

    def __init__(self,size,hero=None,nbrooms=200):
        self.size=size
        self._hero=hero
        self._mat=[]
        self._roomsToReach=[]
        self._rooms=[]
        if self._hero==None:
            self._hero=Hero()
        self.hero=self._hero
        self._nbrooms=nbrooms
        for i in range(self.size) :
            self._mat.append([Map.empty]*self.size)
        self.generateRooms(nbrooms)
        self.reachAllRooms()
        self._elem={}
        self.put(self._rooms[0].center(),self._hero)
        self.hero.coord = self._rooms[0].center()
        for i in self._rooms:
           i.decorate(self)
        print(self)
        
    def checkCoord(self,c) :
        if not(isinstance(c,Coord)):
            raise TypeError('Not a Coord')
        if not(c in self):
            raise IndexError('Out of map coord')
    
    def checkElement(self,e):
        if not(isinstance(e,Element)):
            raise TypeError('Not a Element')
        
        
    def __repr__(self):
        e=""
        for a in range (len(self._mat)): 
            for i in range (self.size) :
                e+=str(self._mat[a][i])
            e+='\n'
        return e

    def __len__(self):
        return self.size

    def __contains__(self,item):
        if(isinstance(item,Coord)):
             return(item.x<self.size and item.y<self.size and item.x>=0 and item.y>=0)
        elif(type(item)==str):
            if(self._elem.get(item)):
                return(True)
        return(False)

    def get(self,c):
        self.checkCoord(c)
        e=self._mat[c.y][c.x]
        return e

    def pos(self,e):
        self.checkElement(e)
        return self._elem.get(e)

    def put(self,c,e):
        self.checkCoord(c)
        self.checkElement(e)
        if e in self._elem :
            raise KeyError('Already placed')
        self._mat[c.y][c.x]=e
        self._elem[e]=c
        return self._elem
        
    def rm(self,c):
        e=self._mat[c.y][c.x]
        self._mat[c.y][c.x]=Map.ground
        if e in self._elem :
            del self._elem[e]
        return self._mat
        
    def move(self, e, way):
        """Moves the element e in the direction way."""
        orig = self.pos(e)
        dest = orig + way
        if dest in self:
            if self.get(dest) == Map.ground:
                self._mat[orig.y][orig.x] = Map.ground
                self._mat[dest.y][dest.x] = e
                self._elem[e] = dest
                if(isinstance(e, Hero)):
                    self.hero.coord = Coord(dest.x, dest.y)
                    self.hero.movement+=1
                    e.modifsasiety()

            elif self.get(dest) != Map.empty and self.get(dest).meet(e) and self.get(dest) != self.hero:
                self.rm(dest)
                return(True)
        return(False)
    
    def moveAllMonsters(self):
        i=0
        k = list(self._elem.keys())
        print(k)
        while(i < len(k)):
            e = k[i]
            i+=1
            if not(isinstance(e,Creature)) or isinstance(e,Hero):
                continue
            
            if not(self.pos(self.hero).distance(self.pos(e))<6):
                continue
            
            if isinstance(e, Creature) and e.name!=self.hero.name:
                if self.get(e.coord+e.coord.direction(self.pos(self.hero)))==Map.ground:
                    e.coord+=e.coord.direction(self.pos(self.hero))

            if(self.move(e,self.pos(e).direction(self.pos(self.hero)))):
                i-=1
            
    def repos(self):
        if self.hero.repos==True :
            i=0
            while i<10 :
                self.moveAllMonsters()
                i+=1
            if self.hero.hp<=self.hero.hp_max :
                self.hero.hp+=5
            else :
                self.hero.hp=self.hero.hp_max
        self.hero.repos=False
        
                

    def addRoom(self,room):
        self._roomsToReach.append(room)
        for i in range(room.c1.y, room.c2.y+1) :
            for a in range (room.c1.x,room.c2.x+1):
                self._mat[i][a]=Map.ground
        return self._mat
                
    def findRoom(self,coord):
        for i in range(len(self._roomsToReach)):
            if coord in self._roomsToReach[i]:
                r=self._roomsToReach[i]
                return r
        return False
    
    def intersectNone(self,room):
        for i in range (len(self._roomsToReach)):
             if room.intersect(self._roomsToReach[i]):
                 return False
        return True
        
    def dig(self,coord):
        self._mat[coord.y][coord.x]=self.ground
        for room in self._roomsToReach:
            if coord in room:
                self._roomsToReach.remove(room)
                self._rooms.append(room)
        
    def corridor(self,start,end):
        dir=1
        if(start.y>end.y):
            dir = -1
        
        for i in range(start.y, end.y+dir, dir):
            self.dig(Coord(start.x, i))
        
        dir=1
        if(start.x>end.x):
            dir=-1
        
        for i in range(start.x, end.x+dir, dir):
            self.dig(Coord(i, end.y))
                
    def reach(self):
        self.corridor(random.choice(self._rooms).center(),random.choice(self._roomsToReach).center())
                
    def reachAllRooms(self):
        self._rooms.append(self._roomsToReach[0])
        self._roomsToReach.pop(0)
        while  len(self._roomsToReach)!=0 :
            self.reach()
            
    def randRoom(self):
        x1=random.randint(1,self.size-3)
        y1=random.randint(1,self.size-3)
        l=random.randint(3,8)
        h=random.randint(3,8)
        return Room(Coord(x1,y1),Coord(min(x1+l,self.size-1),min(y1+h,self.size-1)))
        
    def generateRooms(self,n):
        for i in range (n) :
            room=self.randRoom()
            if self.intersectNone(room) :
                self.addRoom(room)
    
    def key_down_event(self, event):
        self.move(self.hero, Map.dir[event])
        self.moveAllMonsters()
        print(self)


    
    def drawGround(self, SCREEN):
        for ligne in range (len(self._mat)) :
            for case in range (len(self._mat[ligne])) :
                if self._mat[case][ligne]!=Map.empty:
                    SCREEN.blit(self.groundIm, vec(ligne, case)*48)
    
    def drawElem(self,SCREEN):
        from Game import Game
        self.hero.draw(SCREEN)
        self.hero.draw_xp(SCREEN)
        self.hero.draw_sasiety(SCREEN)
        for entity in self._elem :
            entity.draw(Game.SCREEN)


        