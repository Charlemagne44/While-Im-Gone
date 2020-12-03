from World import *
from Player import *

class Model:


	def __init__(self, world, player):
		self.world_object = world
		self.player_object = player

	def parse_choice(self, choice, player, world):

		if(choice == '1' or choice == 1 or choice == 'check inventory' or choice == 'ci' or choice == 'c i' or choice == 'check i' or choice == 'c inventory' or choice == 'c inv'):
			self.check_inventory(player, world)
		elif(choice == '2' or choice == 2 or choice == 'check skills' or choice == 'check skill' or choice == 'cs' or choice == 'c s' or choice == 'check s' or choice == 'c skills' or choice == 'c skill' or choice == 'c sk'):
			self.check_skills(player)
		elif(choice == '3' or choice == 'look around' or choice == 'l' or choice == 'look' or choice == 'loo' or choice == 'around' or choice == 'lo' or choice == 'l o' or choice == 'look a' or choice == 'l around'):
			self.look_around(player)
		elif(choice == '4' or choice == 'move' or choice == 'm' or choice == 'mo' or choice == 'mov'):
			self.move(player)
		elif(choice == '5' or choice == 'talk' or choice == 't' or choice == 'ta' or choice == 'tal'):
			self.talk(player)
		else:
			choice = input("try again: ")
			self.parse_choice(choice, player, world)

	def talk(self, player):
		return

	def move(self, player):
		return

	def look_around(self, player):
		return

	def check_skills(self, player):
		print('\n')
		for skill in player.stats:
			print(skill)
		print('\n')

	def check_inventory(self, player, world):
		for item in player.inventory:
			print(item)
		print("\n")
		print("1. Go back")
		print("2. Use item")
		print("3. Drop item")
		x = input("choice: ")
		print("\n")
		if (x == 1 or x == "go back" or x == "back" or x == 'g b' or x == 'go b' or x == 'g'):
			return
		elif (x == 2 or x == "use" or x == "use item" or x == 'u' or x == 'u i'):
			self.use_item(player)
		elif (x == 3 or x == "drop" or x == "drop item" or x == 'd' or x == 'd i'):
			self.drop_item(player, world)


	def use_item(self, player):
		use = input("Which item: ")
		for item in player.inventory:
			if (use == item.name):
				return

	def drop_item(self, player, world):
		drop = input("Drop item: ")



	def choose_item(player, choice):
		print("Which item: ")
		item = input()
		return item

	def pick_up_item(self, player, item_name):

		current_loc_items = self.world_object.places[self.player_object.location]["items"] 

		#remove object from location

		for item in current_loc_items:
			if item.name == item_name:
				self.world_object.places[self.player_object.location]["items"].remove(item) #removes item from locaiton
				self.player_object.inventory[item_name] = item #adds item to player inv

		
