import pygame
import utility

class Health:
	""" It monitors the health of the player spaceship and enemy spaceship."""
	def __init__(self, lives):
		self.lives = lives

	def draw(self, window):
		if self.lives != 0:
			pos = 5
			for x in range(0, self.lives):
				window.blit(utility.heart, (pos, 5))
				pos += 8
		else :
			window.blit(utility.game_over.render(f"G-A-M-E O-V-E-R", 1, (0, 210, 0)), (30, 210))