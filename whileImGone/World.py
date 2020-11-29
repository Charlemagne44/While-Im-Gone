from Item import *

class World:

	def __init__(self, player):
		#self.world_objects = {}
		
		self.places =  {
			"castle yard" : World.create_castle_yard(self), 
			"castle" : World.create_castle(self)
		}
		
		self.init_items(self.places)


	def init_items(self, places):
		self.letter = Item("letter", "An old letter with a wax seal and aged parchment")
		self.sword = Item("iron sword", "A rusty broadsword with a artisian pommel stone")
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