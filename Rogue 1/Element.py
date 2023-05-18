import pygame
import random
import copy

class Element(object):
    aaa = 4
    def __init__(self,name,abbrv=""):
       self.name=name
       self.abbrv=abbrv
       if abbrv=="" :
           self.abbrv=name[0]
       
    
    def __repr__(self) :
        return self.abbrv

    def description(self):
        return "<"+str(self.name)+">"
    
    def meet(self,hero):
        raise NotImplementedError("Not implemented yet")
    
    @staticmethod
    def randElement(collection):
        X=random.expovariate(1/2)
        for x in collection :
            if x<X :
                indice=x
        l=random.choice(collection[indice])
        return l


    

