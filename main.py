import pygame
import sys
import random

pygame.init()
window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Space Invader")
space_craft = pygame.image.load('spaceship.png')
enemy_craft = pygame.image.load('enemy1.png')
space_background_1 = pygame.image.load('spacebg3.jpg')
space_background_2 = pygame.image.load('spacebg3.jpg')
background_music = pygame.mixer.music.load('Space.mp3')
pygame.mixer.music.play(loops = -1)
bullet_sound = pygame.mixer.Sound('bullet_sound.wav')
crash_sound = pygame.mixer.Sound('blast.wav')
clock = pygame.time.Clock()


class SpaceCraft(object):
	def __init__(self, x, y, velocity):
		self.x = x
		self.y = y
		self.velocity = velocity
		self.hitarea = (self.x + 50, self.y + 20, 60, 60)

	def draw(self, window):
		window.blit(space_craft, (self.x, self.y))
		self.hitarea = (self.x + 50, self.y + 20, 60, 60)
		# pygame.draw.rect(window,(255, 0, 0), self.hitarea, 2)

	def youhit(self):
		print("Enemy Hit Your SpaceCraft.")


class EnemySpaceCraft(object):
	def __init__(self, x, y, velocity):
		self.x = x
		self.y = y
		self.velocity = velocity
		self.hitarea = (self.x + 13, self.y - 10 + 20, 60, 60)

	def draw(self, window):
		window.blit(enemy_craft, (self.x, self.y))
		self.hitarea = (self.x + 13, self.y - 10 + 20, 60, 60)
		# pygame.draw.rect(window,(255, 0, 0), self.hitarea, 2)

	def enemyhit(self):
		print("You Hit EnemySpaceCraft.")



class Bullets(object):
	def __init__(self, x, y, radius, colour, velocity):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.velocity = velocity

	def draw(self, window):
		pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius)


# for drawing all elements in the game.
def draw_elements():
	window.blit(space_background_1, (0, yaxis))
	window.blit(space_background_2, (0, yaxis - 765))
	plane.draw(window)
	for bullet in bullets:
		bullet.draw(window)
	for enemy in enemies:
		enemy.draw(window)
	for bullet in enemy_bullets:
		bullet.draw(window)
	
	pygame.display.update()


# Game Object Variables.
plane = SpaceCraft(0, 520, 10)
enemies = list()
bullets = list()
bullet_recoil = 0
fps = 0
enemy_generator = 0
enemy_bullets = list()
yaxis = 0

# Gameloop
while True:

	# FPS manager
	clock.tick(500)
	if yaxis <= 765:
		yaxis += 1
	else:
		yaxis = 0
	# time delay between two enemies.
	if enemy_generator > 0:
		enemy_generator -= 1

	# time delay between two bullets player{POV}
	if bullet_recoil > 0:
		bullet_recoil -= 1

	if fps < 30:
		fps += 1
		bullet_stopper = False
	else:
		fps = 0
		bullet_stopper = True

	# mange the exit point of the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# manage the enemy bullet velocity and distance bullet travel.
	for bullet in enemy_bullets:
		if bullet.y < 580:
			bullet.y += bullet.velocity
		else:
			enemy_bullets.pop(enemy_bullets.index(bullet))

	# manage the hit marker by the enemy bullets.
	for bullet in enemy_bullets:
		if bullet.y < plane.hitarea[1] + plane.hitarea[3] and bullet.y > plane.hitarea[1]:
			if bullet.x < plane.hitarea[0] + plane.hitarea[2] and bullet.x > plane.hitarea[0]:
				plane.youhit()
				enemy_bullets.pop(enemy_bullets.index(bullet))


	# manage the player bullet velocity and distance bullet travel.
	for bullet in bullets:
		# checks weather the user bullet hit any enemy.
		for enemy in enemies:
			if bullet.y < enemy.hitarea[1] + enemy.hitarea[3] and bullet.y > enemy.hitarea[1]:
				if bullet.x < enemy.hitarea[0] + enemy.hitarea[2] and bullet.x > enemy.hitarea[0]:
					enemy.enemyhit()
					crash_sound.play()
					crash_sound.set_volume(0.05)
					bullets.pop(bullets.index(bullet))
					enemies.pop(enemies.index(enemy))
	for bullet in bullets:
		if bullet.y > 20:
			bullet.y -= bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))

	# manage the tajectory of the enemy plane
	for enemy in enemies:
		if (enemy.y < 500) and (0 < enemy.x < 470):
			enemy.y += enemy.velocity
			enemy.x += (enemy.velocity * random.choice([-1, 1]))
			if bullet_stopper:
				enemy_bullets.append(Bullets(enemy.x + 50, enemy.y + 70, 3, (255, 255, 255), 8))
		else:
			enemies.pop(enemies.index(enemy))

	# control no of enemies at a time.
	if len(enemies) < 5:
		if enemy_generator == 0:
			enemies.append(EnemySpaceCraft(random.randint(0, 480), 0, 3))
			enemy_generator = 5


	# key management.
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and plane.x >= -50:
		plane.x -= plane.velocity
		
	if keys[pygame.K_RIGHT] and plane.x < 400:
		plane.x += plane.velocity

	if keys[pygame.K_SPACE]:
		if len(bullets) < 20 and bullet_recoil == 0:
			bullets.append(Bullets(plane.x + 80, plane.y, 3, (255, 255, 255), 20))
			bullet_sound.play()
			bullet_sound.set_volume(0.05)
			bullet_recoil = 3
	draw_elements()
