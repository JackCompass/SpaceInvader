import pygame
import utility

class Bullets:
	""" Class to maintain the bullet objects and its trajectory"""
	def __init__(self, x, y, radius, colour, velocity):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.velocity = velocity

	def draw(self, window):
		pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius)

	def bullet_trajectory():
		for bullet in utility.enemy_bullets:
			if bullet.y < 580:
				bullet.y += bullet.velocity
			else:
				utility.enemy_bullets.pop(utility.enemy_bullets.index(bullet))

	def player_bullet_trajectory():
		for bullet in utility.bullets:
			if bullet.y > 20:
				bullet.y -= bullet.velocity
			else:
				utility.bullets.pop(utility.bullets.index(bullet))

	def bullet_hit():
		for bullet in utility.enemy_bullets:
			if bullet.y < utility.plane.hitarea[1] + utility.plane.hitarea[3] and bullet.y > utility.plane.hitarea[1]:
				if bullet.x < utility.plane.hitarea[0] + utility.plane.hitarea[2] and bullet.x > utility.plane.hitarea[0]:
					utility.lives.lives -= 1
					utility.enemy_bullets.pop(utility.enemy_bullets.index(bullet))

	def enemy_hit():
		for bullet in utility.bullets:
			for enemy in utility.enemies:
				if bullet.y < enemy.hitarea[1] + enemy.hitarea[3] and bullet.y > enemy.hitarea[1]:
					if bullet.x < enemy.hitarea[0] + enemy.hitarea[2] and bullet.x > enemy.hitarea[0]:
						utility.score += 1
						utility.crash_sound.play()
						utility.crash_sound.set_volume(0.05)
						utility.bullets.pop(utility.bullets.index(bullet))
						utility.enemies.pop(utility.enemies.index(enemy))
