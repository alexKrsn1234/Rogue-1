import pygame
import time
import random
from Img import *
from Map import Map
from Coord import Coord
from Stairs import Stairs
from Hero import Hero
from Equipment import Equipment
import time
#Init :
pygame.init()
pygame.font.init()
#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("./Img/icon.png")
pygame.display.set_icon(icon)

vec = pygame.math.Vector2

#Screen :


heroImg=pygame.image.load("./Img/zelda_0.png")
mobImg=pygame.image.load("./Img/magicien.png")
sol = pygame.image.load("./Img/sol1.png")
stairs = pygame.image.load("./Img/escaliers.png")
le_mur = pygame.image.load("./Img/la_muraille_du_kazakstan.png")
#Game Loop :
direction = {pygame.K_z:Coord(0,-1) , pygame.K_d:Coord(1,0), pygame.K_q:Coord(-1,0), pygame.K_s:Coord(0,1)}
heroImg0=pygame.image.load("./Img/zelda_0.png")
clock=pygame.time.Clock()

def heal(creature):
    creature.hp+=3
    return True

def teleport(m, creature, unique):
    m.rm(m.pos(creature))
    r=random.choice(m._rooms)
    c=r.randEmptyCoord(m)
    m.put(c,creature)
    return unique



class Game(object):

    info=pygame.display.Info()
    WIDHT = info.current_w-10
    HEIGHT=info.current_h-50
    Modulo=int(HEIGHT)/48
    SIZE = WIDHT, HEIGHT
    SCREEN=pygame.display.set_mode(SIZE)
    Font1 = pygame.font.SysFont('chalkduster.ttf', 72)
    Font2 = pygame.font.SysFont('chalkduster.ttf', 48)
    
    
    def __init__(self,hero=None,level=1,message=None):
        self.hero=hero
        if self.hero==None:
            self.hero=Hero()
        self._level=level
        print(Game.Modulo)
        self._floor=Map(size=int(Game.Modulo), hero=Hero())
        self._hero=self.hero
        self.buildFloor(self._floor)
        self._message=message
        self.inventory_open=False
        if self._message==None :
            self._message=[]

    
    def addMessage(self,m):
        self._message.append(m)
    
    def readMessages(self):
        totm=""
        for i in range(len(self._message)) :
            totm+=self._message[i]+". "
        self._message=[]
        return totm
        
    def buildFloor(self,m):
        c=m._rooms[-1].center()
        m.put(self._floor._rooms[-1].center(),Stairs(coord=self._floor._rooms[-1].center()))

    def draw_text(self,SCREEN,text,font,text_col,x,y):
        img=font.render(text, True, text_col)
        SCREEN.blit(img, vec(x,y))

    def inventory_draw(self, SCREEN):
        
        self.draw_text(Game.SCREEN, "Inventory", font = Game.Font1, text_col=(255,255,255), x=10, y=10)
        self.draw_text(Game.SCREEN, "Choose an item", font = Game.Font1, text_col=(255,255,255), x=200, y=200)
        for i in range(len(self._floor.hero._inventory)):
            SCREEN.blit(self._floor.hero._inventory[i].Im, vec(10, 70 + i*50))
            self.draw_text(Game.SCREEN,str(i)+" : "+ self._floor.hero._inventory[i].name, font = Game.Font2, text_col=(255,255,255), x=60, y=80 + i*50)
        self.gold_draw(Game.SCREEN)

    def gold_draw(self,SCREEN):
        print(Game.HEIGHT,Game.WIDHT)
        Game.SCREEN.blit(Equipment.Imgold, vec(Game.WIDHT,Game.HEIGHT-100))
        self.draw_text(Game.SCREEN,str(self._floor.hero.gold)+" x Gold", font = Game.Font2, text_col=(255,255,255), x=Game.WIDHT, y=Game.HEIGHT-30)    
    
    
    def chooseInventory(self) :
        for event in pygame.event.get():
            if event.key==pygame.K_0:
                self._floor.hero._inventory[0].use()
            elif event.key==pygame.K_1:
                self._floor.hero._inventory[1].use()
            elif event.key==pygame.K_2:
                self._floor.hero._inventory[2].use()
            elif event.key==pygame.K_3:
                self._floor.hero._inventory[3].use()
            elif event.key==pygame.K_4:
                self._floor.hero._inventory[4].use()
            elif event.key==pygame.K_5:
                self._floor.hero._inventory[5].use()
            elif event.key==pygame.K_6:
                self._floor.hero._inventory[6].use()
            elif event.key==pygame.K_7:
                self._floor.hero._inventory[7].use()
            elif event.key==pygame.K_8:
                self._floor.hero._inventory[8].use()
            elif event.key==pygame.K_9:
                self._floor.hero._inventory[9].use()


    def key_down(self,event):
        if event.key==pygame.K_k:
            pygame.quit()
            exit()

        if event.key==pygame.K_i :
            print((self._floor.hero.strInventory()))
            self.inventory_open = not(self.inventory_open)
        
        if(event.key in (pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d)):
            theGame()._floor.key_down_event(event.key)

        if event.key==pygame.K_u :
            self.chooseInventory()
            

    def play(self):
        while 1:
            #RGB : Red Green Blue
            Game.SCREEN.fill((50,33,37))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
            
                if event.type==pygame.KEYDOWN:
                    self.key_down(event)
                    
                    #if (event.key ==pygame.K_u):
                     #  Game.SCREEN.blit()
                    
        

            Game.SCREEN.blit(le_mur, (0,0))
            theGame()._floor.drawGround(Game.SCREEN)
            theGame()._floor.drawElem(Game.SCREEN)
            Game.SCREEN.blit(heroImg, (theGame()._floor.hero.map_pos.x, theGame()._floor.hero.map_pos.y))
            if(self.inventory_open):
                self.inventory_draw(Game.SCREEN)
            pygame.display.flip()
            clock.tick(2000)
            pygame.display.set_caption(str(int(clock.get_fps())))
    
def theGame(game=Game()) :
    return game






