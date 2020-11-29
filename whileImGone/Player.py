

class Player:

	options = ["check inventory", "check skills", "look around", "move", "talk"]

	def __init__(self, location, playerName, inventory, stats):
		self.location  = location
		self.playerName = playerName
		self.inventory = inventory
		self.stats = stats