from Element import Element
import pygame
from Hero import Hero
import random

def heal(creature):
    creature.hp+=3
    return True

def teleport(m, creature, unique):
    m.rm(m.pos(creature))
    r=random.choice(m._rooms)
    c=r.randEmptyCoord(m)
    m.put(c,creature)
    return unique

class Equipment(Element):
    equipments = {0: [("potion", "!", None, lambda self, hero: heal(hero), False), \
                      ("gold", "o", None, None, False)], \
                  1: [("dagger", "d", None, lambda self, hero: throw(2, False), True, {'strength': 1}), \
                      ("potion", "!", lambda self, hero: teleport(hero, True))], \
                  2: [("sword", "s", None, None, True, {'strength': 2}), \
                      ("bow", "b", None, lambda self, hero: throw(1, True), True, None), \
                      ("leather vest", 'l', None, None, True, {'armor': 1})], \
                  3: [("portoloin", "w" , None, lambda self, hero: teleport(hero, False))],
                  4: [("chaimail", 'c', None, None, True, {'armor': 2})]}
    
    def __init__ (self,name,abbrv="",Im=None,usage=None, weapon=True, effect=None ):
        super().__init__(name,abbrv)
        self.usage=usage
        self.Im=Im
        self.weapon = weapon
        
    def meet(self,hero):
        if isinstance(hero,Hero):
            hero.take(self)
            return True
    
    def use(self,creature):
        if(self.usage == None):
            return(False)
        
        return(self.usage(self, creature))

    @staticmethod
    def randEquipment():
        return Element.randElement(Equipment.equipments)