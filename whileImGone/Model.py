from World import *
from Player import *

class Model:


	def __init__(self, world, player):
		self.world_object = world
		self.player_object = player


	def print_choices(player):
		i = 1
		for option in p.options:
			print(str(i) + ". " + option)
			i += 1
		answer = input("choice: ")

	def parse_choice(choice, player, world):
		options = {
			1 : check_inventory,
			2 : check_skills,
			3 : look_around,
			4 : move,
			5 : talk
		}

		options[choice]()


	def check_inventory(player):
		for item in player.inventory:
			print(item)
		print("\n")
		print("1. Go back")
		print("2. Use item")
		print("3. Drop item")
		x = input("Choice: ")

		if (x == 1 or x == "go back" or x == "back"):
			Model.print_choices(player)
		elif (x == 2 or x == "use" or x == "use item"):
			Model.use_item(player)
		elif (x == 3 or x == "drop" or x == "drop item"):
			Model.drop_item(player)

	def choose_item(player, choice):
		print("Which item: ")
		item = input()

	def pick_up_item(self, player, item_name):

		current_loc_items = self.world_object.places[self.player_object.location]["items"] 

		#remove object from location

		for item in current_loc_items:
			if item.name == item_name:
				self.world_object.places[self.player_object.location]["items"].remove(item) #removes item from locaiton
				self.player_object.inventory[item_name] = item #adds item to player inv
		

		
