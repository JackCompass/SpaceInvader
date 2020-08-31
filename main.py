import pygame
import sys

pygame.init()
window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Space Invader")
space_craft = pygame.image.load('spaceship.png')
space_background = pygame.image.load('spacebg1.jpg')
clock = pygame.time.Clock()


class SpaceCraft(object):
	def __init__(self, x, y, height, width, velocity):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.velocity = velocity

	def draw(self, window):
		window.blit(space_craft, (self.x, self.y))


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
	window.blit(space_background, (0, 0))
	for bullet in bullets:
		bullet.draw(window)
	plane.draw(window)
	pygame.display.update()

# object
plane = SpaceCraft(0, 520, 2, 2, 10)
bullets = list()
bullet_recoil = 0

# Gameloop
while True:
	clock.tick(30)
	if bullet_recoil > 0:
		bullet_recoil -= 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	for bullet in bullets:
		if bullet.y > 20:
			bullet.y -= bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))
		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and plane.x >= -50:
		plane.x -= plane.velocity
		
	if keys[pygame.K_RIGHT] and plane.x < 400:
		plane.x += plane.velocity

	if keys[pygame.K_SPACE]:
		if len(bullets) < 20 and bullet_recoil == 0:
			bullets.append(Bullets(plane.x + 80, plane.y, 3, (255, 255, 255), 20))
			bullet_recoil = 3

	draw_elements()
