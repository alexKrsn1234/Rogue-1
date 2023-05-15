from Element import Element

class Equipment(Element):
    
    def __init__ (self,name,abbrv="",usage=None ):
        super().__init__(name,abbrv)
        self.usage=usage
        
    def meet(self,hero):
        from Game import theGame
        from Hero import Hero
        if isinstance(hero,Hero):
            hero.take(self)
            m="You pick up a "+self.name
            theGame().addMessage(m)
            return True
    
    def use(self,creature):
        from Game import theGame
        if self.usage!=None :
            theGame().addMessage("The "+str(creature.name)+" uses the "+str(self.name))
            return(self.usage(creature))
        if self.abbrv=="!":
            theGame().addMessage("The "+str(creature.name)+" uses the "+str(self.name))
            return heal(creature)
        else:
            theGame().addMessage("The "+str(self.name)+" is not usable")
            return False
