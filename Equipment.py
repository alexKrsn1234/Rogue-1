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

def equip_weapon(hero, weapon):
    if hero.weapon == None:
        hero.weapon = weapon
        hero.strength += weapon.strength
    else:
        hero.strength -= hero.weapon.strength
        hero.weapon = weapon
        hero.strength += weapon.strength
    hero.weapon_durability = 5

    return True

class Equipment(Element):
    equipments = {0: [("potion", "!", None, lambda hero, m, weapon: heal(hero)), \
                      ("gold", "o"), \
                      ("chicken","c")], \
                  1: [("potion_teleport", "?", None, lambda hero, m, weapon: teleport(m, hero, True))], \
                  2: [("sword", "s", None,lambda hero, m, weapon : equip_weapon(hero, weapon), 3)], \
                  3: [("portoloin", "w" , None, lambda hero, m, weapon: teleport(m, hero, False))]}

    Impotion=pygame.image.load("./Img/potion.png")
    Impotiontel=pygame.image.load("./Img/potion_teleport.png")
    Imgold=pygame.image.load("./Img/gold.png")
    Imsword=pygame.image.load("./Img/sword.png")
    Importoloin=pygame.image.load("./Img/portoloin.png")
    Imchicken=pygame.image.load("./Img/chicken.png")
    equipment_liste={"potion" : Impotion, "potion_teleport" : Impotiontel, "gold" : Imgold,"sword": Imsword, "portoloin" : Importoloin, "chicken" : Imchicken}
    
    def __init__ (self,name,abbrv="",Im=None,usage=None, strength = 0, coord = None ):
        super().__init__(name,coord,abbrv)
        self.usage=usage
        self.Im=Equipment.equipment_liste[self.name]
        self.strength = strength

    
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
            return(self.usage(creature, m, self))

    @staticmethod
    def randEquipment():
        return Element.randElement(Equipment.equipments)