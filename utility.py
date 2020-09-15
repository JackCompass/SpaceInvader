import pygame
import spaceship
import health

"""Loading all the images and sound"""
pygame.init()
window = pygame.display.set_mode((500, 600))
icon = pygame.image.load('icon.png')
space_craft = pygame.image.load('spaceship.png')
enemy_craft = pygame.image.load('enemy1.png')
space_background_1 = pygame.image.load('spacebg3.jpg')
space_background_2 = pygame.image.load('spacebg3.jpg')
pygame.mixer.music.load('Space.mp3')
bullet_sound = pygame.mixer.Sound('bullet_sound.wav')
crash_sound = pygame.mixer.Sound('blast.wav')
heart = pygame.image.load('life.png')
font = pygame.font.SysFont("roboto", 20, bold = True, italic = True)
game_over = pygame.font.SysFont("roboto", 50, bold = True)
pygame.display.set_caption("SpaceInvader")
pygame.display.set_icon(icon)
pygame.mixer.music.play(loops = -1)
clock = pygame.time.Clock()


"""Variables used to control the game. """
plane = spaceship.SpaceCraft(0, 520, 10)
lives = health.Health(10)
enemies = list()
enemy_bullets = list()
bullets = list()
bullet_recoil = 0
enemy_generator = 0
score = 0
fps = 0
space_background_width = 0
bullet_stopper = True

""" It blits all the objects and their respective components."""
def draw_elements():
	window.blit(space_background_1, (0, space_background_width))
	window.blit(space_background_2, (0, space_background_width - 765))
	window.blit(font.render(f"score : {score}", 1, (255, 255, 255)), (380, 10))
	plane.draw(window)
	lives.draw(window)
	for bullet in bullets:
		bullet.draw(window)
	for enemy in enemies:
		enemy.draw(window)
	for bullet in enemy_bullets:
		bullet.draw(window)
	
	pygame.display.update()

	
