from Item import *

class World:

	

	def __init__(self, player):
		#self.world_objects = {}
		self.letter_desc = open(r"Resources\Descriptions\Items\intro_letter_desc.txt")
		self.letter_text = open(r"Resources\TextItems\intro_letter_desc.txt")
		self.sword_desc = open(r"Resources\Descriptions\Items\rusty_broadsword.txt")
		self.places =  {
			"castle yard" : World.create_castle_yard(self), 
			"castle" : World.create_castle(self)
		}
		
		self.init_items(self.places)


	def init_items(self, places):
		self.letter = TextItem("letter", self.letter_desc, 't', self.letter_text) #self, name, desc, type, text
		self.sword = WeaponItem("iron sword", "", 'w', 5, 1, 0) #self, name, desc, type, damage, strength_req, agil_req
		self.places["castle yard"]["items"].append(self.sword)
		self.places["castle yard"]["items"].append(self.letter)
		
	def create_castle_yard(self):
		castleYard = {
			"name" : "castle yard",
			"items" : [],
			"friends" : ["benton"],
			"visited" : False
		}
		return castleYard
	def create_castle(self):
		castle = {
			"name" : "castle",
			"items" : [],
			"friends" : [],
			"actions" : [],
			"visited" : False
		}