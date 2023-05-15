from Element import Element
from Equipment import Equipment
from Creature import Creature

class Hero(Creature):
    def __init__(self,name="Hero",hp=10,abbrv="@",strength=2,inventory=None):
        super().__init__(name,hp,abbrv,strength)
        self._inventory=inventory
        if self._inventory==None:
            self._inventory=[]
        self.name=self.name
            
    def description(self):
       return super().description()+str(self._inventory)

    def take(self,e):
        if not (isinstance(e,Equipment)) :
            raise TypeError('Not a Equipment')
        return self._inventory.append(e)
    
    def use(self,item):
        if not (isinstance(item,Equipment)) :
            raise TypeError('Not a Equipment')
        if not (item in self._inventory):
            raise ValueError('Not in inventory')
        if item.use(self) :
            self._inventory.pop(self._inventory.index(item))

    def fullDescription(self):
        l=""
        for i in self.__dict__:
            l+=f"> {i[1:] if(i[0]=='_') else i} : {self.__dict__[i]}\n" if(i != "_inventory") else ""
        l+=f"> INVENTORY : {[i.name for i in self._inventory]}"
        return l
        
