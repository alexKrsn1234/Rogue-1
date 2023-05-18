from Element import Element

class Stairs(Element):
    def __init__(self,name="Stairs",abbrv="E"):
        super().__init__(name,abbrv)
    
    def __repr__(self):
        return super().__repr__()
    
    def description(self):
        return super().description()
    
    def meet(self,other):
        from Game import theGame
        theGame().buildFloor()
        theGame().addMessage("The "+str(other.name)+" goes down")
