import pygame
import utility
import random
import shooter

class SpaceCraft(object):
	""" """
	def __init__(self, x, y, velocity):
		self.x = x
		self.y = y
		self.velocity = velocity
		self.hitarea = (self.x + 50, self.y + 20, 60, 60)

	def draw(self, window):
		window.blit(utility.space_craft, (self.x, self.y))
		self.hitarea = (self.x + 50, self.y + 20, 60, 60)

class EnemySpaceCraft(object):
	""" """
	def __init__(self, x, y, velocity):
		self.x = x
		self.y = y
		self.velocity = velocity
		self.hitarea = (self.x + 13, self.y - 10 + 20, 60, 60)

	def draw(self, window):
		window.blit(utility.enemy_craft, (self.x, self.y))
		self.hitarea = (self.x + 13, self.y - 10 + 20, 60, 60)

	def trajectory(bullet_stopper):
		for enemy in utility.enemies:
			if (enemy.y < 500) and (0 < enemy.x < 470):
				enemy.y += enemy.velocity
				enemy.x += (enemy.velocity * random.choice([-1, 1]))
				if bullet_stopper:
					utility.enemy_bullets.append(shooter.Bullets(enemy.x + 50, enemy.y + 70, 3, (255, 255, 255), 8))
			else:
				utility.enemies.pop(utility.enemies.index(enemy))
	
	def total_enemies():
		if len(utility.enemies) < 5:
			if utility.enemy_generator == 0:
				utility.enemies.append(EnemySpaceCraft(random.randint(0, 480), 0, 3))
				utility.enemy_generator = 5