import pygame
import time
import random
from Img import *
from gestion_map.Map import Map
from autre.Coord import Coord
from gestion_map.Stairs import Stairs
from elements_jeu.Hero import Hero
from elements_jeu.Equipment import Equipment
import time
#Init :
pygame.init()
pygame.font.init()
#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("./Rogue 1/Img/icon.png")
pygame.display.set_icon(icon)

vec = pygame.math.Vector2



heroImg=pygame.image.load("./Rogue 1/Img/zelda_0.png")
mobImg=pygame.image.load("./Rogue 1/Img/magicien.png")
sol = pygame.image.load("./Rogue 1/Img/sol1.png")
stairs = pygame.image.load("./Rogue 1/Img/escaliers.png")
le_mur = pygame.image.load("./Rogue 1/Img/la_muraille_du_kazakstan.png")
direction = {pygame.K_z:Coord(0,-1) , pygame.K_d:Coord(1,0), pygame.K_q:Coord(-1,0), pygame.K_s:Coord(0,1)}
heroImg0=pygame.image.load("./Rogue 1/Img/zelda_0.png")
clock=pygame.time.Clock()
game_over=pygame.image.load("./Rogue 1/Img/game_over.png")



class Game(object):

    info=pygame.display.Info()
    WIDHT = info.current_w-10
    HEIGHT=info.current_h-50
    Modulo=HEIGHT//48
    SIZE = WIDHT, HEIGHT
    SCREEN=pygame.display.set_mode(SIZE)#, pygame.FULLSCREEN)
    Font1 = pygame.font.SysFont('chalkduster.ttf', 30)
    Font2 = pygame.font.SysFont('chalkduster.ttf', 25)
    key_dictionnary_number = {pygame.K_0 : 0, pygame.K_1 : 1, pygame.K_2 : 2, pygame.K_3 : 3, pygame.K_4 : 4, pygame.K_5 : 5, pygame.K_6: 6, pygame.K_7 : 7, pygame.K_8 : 8, pygame.K_9 : 9}
    
    def __init__(self,hero=None,level=1,message=None):
        self.hero=hero
        if self.hero==None:
            self.hero=Hero()
        self._level=level
        self._floor=Map(size=Game.Modulo, hero=self.hero)
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
        if(self.inventory_open):
            self.draw_text(Game.SCREEN, "Inventory : Choose an item", font = Game.Font1, text_col=(255,255,255), x=Game.WIDHT/2+Game.WIDHT/5+50, y=20)
            for i in range(len(self._floor.hero._inventory)):
                SCREEN.blit(self._floor.hero._inventory[i].Im, vec(Game.WIDHT/4+Game.WIDHT/2+20, 70 + i*50))
                self.draw_text(Game.SCREEN,str(i)+" : "+ self._floor.hero._inventory[i].name, font = Game.Font2, text_col=(255,255,255), x=Game.WIDHT/4+Game.WIDHT/2+80, y=90 + i*50)
            self.gold_draw(Game.SCREEN)

    def gold_draw(self,SCREEN):
        Game.SCREEN.blit(Equipment.Imgold, vec(Game.WIDHT/2+Game.WIDHT/5, Game.HEIGHT-Game.HEIGHT/7-20))
        self.draw_text(Game.SCREEN,str(self._floor.hero.gold)+" x Gold", font = Game.Font2, text_col=(255,255,255), x=Game.WIDHT/2+Game.WIDHT/5+60, y=Game.HEIGHT-Game.HEIGHT/7)    


    def key_down(self,event):
        if event.key==pygame.K_k:
            Game.SCREEN.blit(game_over,(Game.WIDHT/2,Game.HEIGHT/2))
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            exit()

        if event.key==pygame.K_i :
            print((self._floor.hero.strInventory()))
            self.inventory_open = not(self.inventory_open)
        
        if event.key==pygame.K_SPACE :
            self._floor.repos()

                
        if(event.key in (pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d)):
            self._floor.key_down_event(event.key)

        if(self.inventory_open and event.key in Game.key_dictionnary_number):
            key = Game.key_dictionnary_number[event.key]
            print(key, self._hero._inventory)
            if(key >= len(self._hero._inventory)):
                return
            self._hero._inventory[key].use(self._floor.hero, self._floor)
            if self._hero._inventory[key].use(self._floor.hero, self._floor)== True: 
                self._floor.hero._inventory.pop(self._floor.hero._inventory.index(self._hero._inventory[key]))

            self.inventory_open=False
            

    def play(self):
        while 1:
            #RGB : Red Green Blue
            Game.SCREEN.fill((50,33,37))
            events = pygame.event.get()
            for event in events:
                if event.type==pygame.QUIT :
                    pygame.quit()
                    exit()

                if self._floor.hero.hp<=0:
                    Game.SCREEN.blit(game_over,(Game.WIDHT/2,Game.HEIGHT/2))
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.quit()
                    exit()

                if event.type==pygame.KEYDOWN:
                    self.key_down(event)
                    
        

            Game.SCREEN.blit(le_mur, (0,0))
            self._floor.drawGround(Game.SCREEN)
            self._floor.drawElem(Game.SCREEN)
            self.inventory_draw(Game.SCREEN)
            pygame.display.flip()
            clock.tick(200000)
            pygame.display.set_caption(str(int(clock.get_fps())))
    
def theGame(game=Game()) :
    return game






