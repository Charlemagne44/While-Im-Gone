import time
import winsound


class View:

	def intro_to_game():
		intro1 = open(r"C:\Users\Owner\source\repos\whileImGone\whileImGone\Resources\Text\introPt1.txt")
		intro2 = open(r"C:\Users\Owner\source\repos\whileImGone\whileImGone\Resources\Text\introPt2.txt")
		castle = open(r"C:\Users\Owner\source\repos\whileImGone\whileImGone\Resources\Art\castle.txt")
		rodnar = open(r"C:\Users\Owner\source\repos\whileImGone\whileImGone\Resources\Art\rodnar.txt")

		winsound.PlaySound(r"C:\Users\Owner\source\repos\whileImGone\whileImGone\Resources\Sound\sound1.wav", winsound.SND_ASYNC)

		time.sleep(3)
		View.slow_print_text(intro1.readlines())
		View.slow_print_ascii(castle.readlines())
		View.slow_print_text(intro2.readlines())
		View.slow_print_ascii(rodnar.readlines())

	def slow_print_text(text):
		for line in text:
			for c in line:
				if(c == '.' or c== '?'):
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
		


		