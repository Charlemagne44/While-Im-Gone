from View import *
from World import *
from Player import *
from Model import *
import winsound

#import Model


class Controller:

	def main():
		running = True
		p = Player("castle yard", "", [], {"speech" : 0, "strength" : 0, "agility" : 0})
		v = View()
		m = Model(World(p), p)
		v.intro_to_game()
		v.frog_theme()
		while(running):
			i = 1
			for option in p.options:
				print(str(i) + ". " + option)
				i += 1
			running = False
		answer = input("choice: ")
			
	
	if __name__ == "__main__":
		main()