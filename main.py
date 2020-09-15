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

		# Controls the Infinite loop of the background.
		if utility.space_background_width <= 765:
			utility.space_background_width += 2
		else:
			utility.space_background_width = 0

		spaceship.EnemySpaceCraft.delay()
		shooter.Bullets.recoil()
		shooter.Bullets.enemy_bullet_recoil()
		
		# Manage the exit of the game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		spaceship.EnemySpaceCraft.trajectory(utility.bullet_stopper)
		spaceship.EnemySpaceCraft.total_enemies()
		shooter.Bullets.bullet_trajectory()
		shooter.Bullets.player_bullet_trajectory()

		if utility.lives.lives > 0:
			shooter.Bullets.bullet_hit()
			shooter.Bullets.enemy_hit()

			""" Key Management """
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT] and utility.plane.x >= -50:
				utility.plane.x -= utility.plane.velocity
				
			if keys[pygame.K_RIGHT] and utility.plane.x < 400:
				utility.plane.x += utility.plane.velocity

			if keys[pygame.K_SPACE]:
				if len(utility.bullets) < 20 and utility.bullet_recoil == 0:
					utility.bullets.append(shooter.Bullets(utility.plane.x + 80, utility.plane.y, 3, (255, 255, 255), 20))
					utility.bullet_sound.play()
					utility.bullet_sound.set_volume(0.05)
					utility.bullet_recoil = 3
		utility.draw_elements()
