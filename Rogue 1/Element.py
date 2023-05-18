import pygame

class Element(object):
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
    


    


