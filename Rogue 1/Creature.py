from Element import Element

class Creature(Element):
    
    def __init__(self,name,hp,abbrv="",Im=None,strength=-1):
        super().__init__(name,abbrv,Im)
        self.hp=hp
        self.strength=strength
        if self.strength==-1:
            self.strength=1
    
    def description(self):
        return super().description()+"("+str(self.hp)+")"
    
    def meet(self,other):
        from Game import theGame
        self.hp-=other.strength
        m="The "+other.name+" hits the "+self.description()
        theGame().addMessage(m)
        return  (self.hp<=0)
