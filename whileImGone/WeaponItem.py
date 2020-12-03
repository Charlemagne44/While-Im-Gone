from Item import *

class WeaponItem(Item):

    def __init__(self, name, desc, type, damage, strength_req, agil_req):
        self.damage = damage
        self.strength_req = strength_req
        self.agil_req = agil_req
        super.__init__(self, name, desc, type)