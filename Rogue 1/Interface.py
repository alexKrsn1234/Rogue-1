import pygame

#Init :
pygame.init()

#Title and Icon :
pygame.display.set_caption("Hunger Games")
icon=pygame.image.load("Sword.png")
pygame.display.set_icon(icon)

#Screen :
screen=pygame.display.set_mode((800,600))

#Player :
playerImg=pygame.image.load("Sword.png")
mobImg=pygame.image.load("Sword.png")
playerX=400
playerY=300
monsterX=0
monsterY=0
playerX_change=0
playerY_change=0
monsterY_change=0
monsterX_change=0

def player(x,y):
     screen.blit(playerImg,(x,y))

def moveMonsterInterface(x,y):
    screen.blit(mobImg,(x,y))

#Game Loop :
running=True
while running:
    #RGB : Red Green Blue
    screen.fill((0,0,0))

    for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                running=False
    
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_q:
                    playerX_change=-0.2
                if event.key==pygame.K_d:
                    playerX_change=0.2
                if event.key==pygame.K_s:
                    playerY_change=0.2
                if event.key==pygame.K_z:
                    playerY_change=-0.2
            if event.type==pygame.KEYUP :
                 if event.key==pygame.K_q or event.key==pygame.K_d or event.key==pygame.K_s or event.key==pygame.K_z :
                    playerY_change=0
                    playerX_change=0 
    
    playerY+=playerY_change
    playerX+=playerX_change               
    player(playerX,playerY)
    moveMonsterInterface(monsterX,monsterY)
    pygame.display.update()


