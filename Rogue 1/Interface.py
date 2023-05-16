import pygame
import time

#Init :
pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load(r'audio\Menu_Music.mp3')
#pygame.mixer.music.play(-1)
#   pygame.mixer.music.set_volume(1.0)

#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Screen :
screen=pygame.display.set_mode((800,600))

#Player :

heroImg=pygame.image.load("zelda_0.png")
mobImg=pygame.image.load("magicien.png")
playerX=400
playerY=300
monsterX=0
monsterY=0
playerX_change=0
playerY_change=0
monsterY_change=0
monsterX_change=0

frameHaut=[ pygame.image.load("zelda_"+str(i)+"_haut.png") for i in range(3)]
frameBas=[ pygame.image.load("zelda_"+str(i)+"_bas.png") for i in range(3)]
frameDroite=[ pygame.image.load("zelda_"+str(i)+"_droite.png") for i in range(3)]
frameGauche=[ pygame.image.load("zelda_"+str(i)+"_gauche.png") for i in range(3)]

def player(x,y,n,way):
    screen.blit(heroImg,(x,y))

def moveMonsterInterface(x,y):
    screen.blit(mobImg,(x,y))

#Game Loop :
running=True
i=0
way=""
a=0
heroImg=pygame.image.load("zelda_0.png")
clock=pygame.time.Clock().get_fps()
while running:
    #RGB : Red Green Blue
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False   
    
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_q:
                    playerX_change=-0.1
                    i+=1
                    a=i%4
                    heroImg=frameGauche[a]
                    if clock.tick(2) :
                        i+=1
                if event.key==pygame.K_d:
                    playerX_change=0.1
                    i+=1
                    a=i%4
                    way="_droite"
                if event.key==pygame.K_s:
                    playerY_change=0.1
                    i+=1
                    a=i%4
                    way="_bas"
                if event.key==pygame.K_z:
                    playerY_change=-0.1
                    
            if event.type==pygame.KEYUP :
                 heroImg=pygame.image.load("zelda_0.png")
                 if event.key==pygame.K_q or event.key==pygame.K_d or event.key==pygame.K_s or event.key==pygame.K_z :
                    a=0
                    way=""
                    playerY_change=0
                    playerX_change=0 
                   
    playerY+=playerY_change
    playerX+=playerX_change               
    player(playerX,playerY,a,way)
    pygame.display.update()


