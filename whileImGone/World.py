

class World:

	def __init__(self, player):
		self.places = World.init_world(player)


	def init_world(player):
		world = {
			"castle yard" : World.create_castle_yard(), 
			"castle" : World.create_castle()}
		return world
		
	def create_castle_yard():
		castleYard = {
			"name" : "castle yard",
			"items" : ["sword"],
			"friends" : ["rodnar"],
			"visited" : False
		}
		return castleYard
	def create_castle():
		castle = {
			"name" : "castle",
			"items" : [],
			"friends" : [],
			"actions" : [],
			"visited" : False
		}