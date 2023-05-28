import pygame
import random
import copy

vec = pygame.math.Vector2
class Element(pygame.sprite.Sprite):
    aaa = 4
    def __init__(self,name,coord, abbrv=""):
       super().__init__()
       self.name=name
       self.abbrv=abbrv
       self.coord = coord
       if abbrv=="" :
           self.abbrv=name[0]
       
    
    def __repr__(self) :
        return self.abbrv

    def description(self):
        return "<"+str(self.name)+">"
    
    def meet(self,hero):
        raise NotImplementedError("Not implemented yet")
    
    def draw(self,SCREEN) :
        if(self.Im != None):
            SCREEN.blit(self.Im,vec(self.coord.x, self.coord.y)*48)

    @staticmethod
    def randElement(collection):
        X=random.expovariate(1/2)
        for x in collection :
            if x<X :
                indice=x
        l=random.choice(collection[indice])
        return l


    

