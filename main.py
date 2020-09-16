import pygame
import sys
import random
import utility
import health
import spaceship
import shooter


if __name__ == "__main__":

	# Gameloop
	while True:

		# Control Frame Per Second
		utility.clock.tick(40)

		# Manage the exit of the game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		""" Key Management """
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			utility.game_pause = True
		if keys[pygame.K_DOWN]:
			utility.game_pause = False

		if not utility.game_pause:
		
			if keys[pygame.K_LEFT] and utility.plane.x >= -50:
				utility.plane.x -= utility.plane.velocity
				
			if keys[pygame.K_RIGHT] and utility.plane.x < 400:
				utility.plane.x += utility.plane.velocity

			if keys[pygame.K_SPACE]:
				if len(utility.bullets) < 20 and utility.bullet_recoil == 0:
					utility.bullets.append(shooter.Bullets(utility.plane.x + 50, utility.plane.y, 3, (255, 255, 255), 20))
					utility.bullet_sound.play()
					utility.bullet_sound.set_volume(0.05)
					utility.bullet_recoil = 3
			if keys[pygame.K_LCTRL]:
				if utility.fps == 0:
					utility.plane.change()

			# Controls the Infinite loop of the background.
			if utility.space_background_width <= 765:
				utility.space_background_width += 2
			else:
				utility.space_background_width = 0

			spaceship.EnemySpaceCraft.total_enemies()
			shooter.Bullets.player_bullet_trajectory()
			spaceship.EnemySpaceCraft.trajectory(utility.bullet_stopper)
			shooter.Bullets.enemy_bullet_recoil()
			spaceship.EnemySpaceCraft.delay()
			shooter.Bullets.recoil()
			shooter.Bullets.bullet_trajectory()
			if utility.lives.lives > 0:
				shooter.Bullets.bullet_hit()
				shooter.Bullets.enemy_hit()

		
		utility.draw_elements()
