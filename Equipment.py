from Element import Element
import pygame
from Hero import Hero
import random

def heal(creature):
    if creature.hp+10>=creature.hp_max :
        creature.hp=creature.hp_max
    else :
        creature.hp+=10
    return True


def teleport(m, creature, unique):
    m.rm(m.pos(creature))
    r=random.choice(m._rooms)
    c=r.randEmptyCoord(m)
    m.put(c,creature)
    return unique


def modifstrength(m,n,unique) :
    m.hero.strength+=n
    return unique

class Equipment(Element):
    equipments = {0: [("potion", "!", None, lambda self, hero: heal(hero), False), \
                      ("gold", "o", None, None, False)], \
                  1: [("potion_teleport", "?", None, lambda hero, m: teleport(m, hero, True))], \
                  2: [("sword", "s", None, lambda hero, m : modifstrength(m,5, False))], \
                  3: [("portoloin", "w" , None, lambda hero, m: teleport(m, hero, False))]}

    Impotion=pygame.image.load("./Img/potion.png")
    Impotiontel=pygame.image.load("./Img/potion_teleport.png")
    Imgold=pygame.image.load("./Img/gold.png")
    Imsword=pygame.image.load("./Img/sword.png")
    Importoloin=pygame.image.load("./Img/portoloin.png")
    equipment_liste={"potion" : Impotion, "potion_teleport" : Impotiontel, "gold" : Imgold,"sword": Imsword, "portoloin" : Importoloin}
    
    def __init__ (self,name,abbrv="",Im=None,usage=None, weapon=True, effect=None, strength=-1, coord = None ):
        super().__init__(name,coord,abbrv)
        self.usage=usage
        self.weapon = weapon
        self.strength = strength
        if self.strength==-1:
            self.strength=1
        self.Im=Equipment.equipment_liste[self.name]

    
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