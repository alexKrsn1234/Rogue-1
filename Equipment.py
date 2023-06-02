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
    print("ttt")
    m.rm(m.pos(creature))
    r=random.choice(m._rooms)
    c=r.randEmptyCoord(m)
    m.put(c,creature)
    creature.coord = c
    return unique


def modifstrenght(hero,n):
        hero.strength+=n


class Equipment(Element):
    equipments = {0: [("potion", "!", None, lambda hero, m: heal(hero), False), \
                      ("gold", "o", None, None, False), \
                      ("chicken","c",None, False)], \
                  1: [("potion_teleport", "?", None, lambda hero, m: teleport(m, hero, True))], \
                  2: [("sword", "s", None,lambda hero, m : modifstrenght(hero, 3, ))], \
                  3: [("portoloin", "w" , None, lambda hero, m: teleport(m, hero, False))]}

    Impotion=pygame.image.load("./Img/potion.png")
    Impotiontel=pygame.image.load("./Img/potion_teleport.png")
    Imgold=pygame.image.load("./Img/gold.png")
    Imsword=pygame.image.load("./Img/sword.png")
    Importoloin=pygame.image.load("./Img/portoloin.png")
    Imchicken=pygame.image.load("./Img/chicken.png")
    equipment_liste={"potion" : Impotion, "potion_teleport" : Impotiontel, "gold" : Imgold,"sword": Imsword, "portoloin" : Importoloin, "chicken" : Imchicken}
    
    def __init__ (self,name,abbrv="",Im=None,usage=None, weapon=False, effect=None, coord = None ):
        super().__init__(name,coord,abbrv)
        self.usage=usage
        self.weapon = weapon
        self.Im=Equipment.equipment_liste[self.name]

    
    def meet(self,hero):
        if isinstance(hero,Hero):
            hero.take(self)
            if self.name=="chicken":
                hero.sasiety=hero.sasiety_max
            return True
    
    def use(self,creature, m):
        if(self.usage == None):
            return(False)
        else :
            return(self.usage(creature, m))

    @staticmethod
    def randEquipment():
        return Element.randElement(Equipment.equipments)