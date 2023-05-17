import pygame
import time
from Img import *
from Map import Map

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
screen=pygame.display.set_mode((800,600))

#Player :

heroImg=pygame.image.load("./Img/zelda_0.png")
mobImg=pygame.image.load("./Img/magicien.png")
wall = pygame.image.load("./Img/mur.png")
sol = pygame.image.load("./Img/Sol.png")
playerX=400
playerY=300
monsterX=0
monsterY=0
playerX_change=0
playerY_change=0
monsterY_change=0
monsterX_change=0

frameHaut=[pygame.image.load("./Img/zelda_"+str(i)+"_haut.png") for i in range(4)]
frameBas=[pygame.image.load("./Img/zelda_"+str(i)+"_bas.png") for i in range(4)]
frameDroite=[pygame.image.load("./Img/zelda_"+str(i)+"_droite.png") for i in range(4)]
frameGauche =[pygame.image.load("./Img/zelda_"+str(i)+"_gauche.png") for i in range(4)]
#Game Loop :
direction = {pygame.K_z:vec(0,-1) , pygame.K_d:vec(1,0), pygame.K_q:vec(-1,0), pygame.K_s:vec(0,1)}
heroImg0=pygame.image.load("./Img/zelda_0.png")
clock=pygame.time.Clock()
player_coord = vec(300,300)
actual_frame = 0
counter = 0
m = Map(5)
while 1:
    #RGB : Red Green Blue
    screen.fill((50,33,37))
    m.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
        if event.type==pygame.KEYDOWN :
            heroImg=heroImg0
            pass
    
    counter += 1
    if(counter == 12):
        counter = 0
        actual_frame += 1
        if(actual_frame == 4):
            actual_frame = 0
    
    keys=pygame.key.get_pressed()        
    for key in direction:
        if(keys[key]):
            player_coord+=direction[key]*5
            if(key == pygame.K_z):
                heroImg=frameHaut[actual_frame]
            
            elif(key == pygame.K_q):
                heroImg=frameGauche[actual_frame]

            elif(key == pygame.K_s):
                heroImg=frameBas[actual_frame]
                
            elif(key == pygame.K_d):
                heroImg=frameDroite[actual_frame]
            
            break
        
    screen.blit(heroImg, player_coord)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption(str(int(clock.get_fps())))


