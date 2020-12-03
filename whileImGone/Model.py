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

	def parse_choice(self, choice, player, world):
		options = {
			#1 : self.check_inventory(player),
			#2 : self.check_skills(player),
			#3 : self.look_around,
			#4 : self.move,
			#5 : self.talk
		}

		if(choice == '1' or choice == 1 or choice == 'check inventory' or choice == 'ci' or choice == 'c i' or choice == 'check i' or choice == 'c inventory' or choice == 'c inv'):
			self.check_inventory(player)
		elif(choice == '2' or choice == 2 or choice == 'check skills' or choice == 'check skill' or choice == 'cs' or choice == 'c s' or choice == 'check s' or choice == 'c skills' or choice == 'c skill' or choice == 'c sk'):
			self.check_skills(player)


	def check_skills(self, player):
		print('\n')
		for skill in player.stats:
			print(skill)
		print('\n')

	def check_inventory(self, player):
		for item in player.inventory:
			print(item)
		print("\n")
		print("1. Go back")
		print("2. Use item")
		print("3. Drop item")
		x = input("choice: ")
		print("\n")
		if (x == 1 or x == "go back" or x == "back"):
			Model.print_choices(player)
		elif (x == 2 or x == "use" or x == "use item"):
			Model.use_item(player)
		elif (x == 3 or x == "drop" or x == "drop item"):
			Model.drop_item(player)


	def use_item(player):
		return


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

		
