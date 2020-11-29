import time
import winsound
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
import random


class View:

	def intro_to_game(self):
		intro1 = open(r"Resources\Text\introPt1.txt")
		intro2 = open(r"Resources\Text\introPt2.txt")
		castle = open(r"Resources\Art\castle.txt")
		rodnar = open(r"Resources\Art\benton.txt")

		winsound.PlaySound(r"Resources\Sound\sound1.wav", winsound.SND_ASYNC) #take out loop

		time.sleep(3)
		View.slow_print_text(intro1.readlines())
		View.slow_print_ascii(castle.readlines())
		time.sleep(2)
		View.slow_print_text(intro2.readlines())
		time.sleep(1)
		View.slow_print_ascii(rodnar.readlines())
		time.sleep(1)

	def demo(screen):
		effects = [
			Cycle(
				screen,
				FigletText("ASCIIMATICS", font='big'),
				int(screen.height / 2 - 8)),
			Cycle(
				screen,
				FigletText("ROCKS!", font='big'),
				int(screen.height / 2 + 3)),
			#Stars(screen, 200)
		]
		screen.play([Scene(effects, 500)])


	def slow_print_text(text):
		for line in text:
			for c in line:
				if(c == '.' or c== '?' or c == '!'):
					time.sleep(1)
					print(c, end = "")
				else:
					time.sleep(0.03)
					print(c, end ="")

	def slow_print_ascii(text):
		for line in text:
			time.sleep(0.03)
			for c in line:
				print(c, end = "")
	
				
	def frog_theme(self):
		winsound.PlaySound(r"Resources\Sound\frog_loop.wav", winsound.SND_ASYNC)


		