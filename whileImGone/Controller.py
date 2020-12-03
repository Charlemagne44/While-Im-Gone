from View import *
from World import *
from Player import *
from Model import *
from Item import *
import winsound
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

class Controller:

	def main():
		running = True
		p = Player("castle yard", "", {}, {"speech" : 0, "strength" : 0, "agility" : 0})
		v = View()
		m = Model(World(p), p)

		#inventory testing
		#print(m.world_object.places["castle yard"]["items"])
		m.pick_up_item(p, "letter", 't')
		#print(m.world_object.places["castle yard"]["items"])
		#print(m.player_object.inventory)

		#v.intro_to_game()
		#v.frog_theme()
		running = True
		while(running):
			v.display_choices(p)
			choice = input("choice: ")
			print('\n')
			m.parse_choice(choice, p, m.world_object)

			
	
	if __name__ == "__main__":
		main()