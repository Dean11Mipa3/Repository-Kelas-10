import pygame
import sys
from random import choice

from settings import Settings
from land import Land
from bird import Bird


land = Land()

class Pipe():

	def __init__(self, position):

		self.rect = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
		self.head_rect = pygame.Rect(0, 0, 1.2*self.rect.width, 0.15*self.rect.height)
		self.position = position
		self.color = (0, 200, 0)

		if self.position == "top":
			self.rect.topright = screen_rect.topright
			self.head_rect.midbottom = self.rect.midbottom
		elif position == "bottom":
			self.rect.bottomright = screen_rect.bottomright
			self.head_rect.midtop = self.rect.midtop
	def move(self):
		self.rect.x -= 5

		if self.position == "top":
			self.head_rect.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.head_rect.midtop = self.rect.midtop

	def show(self):
		pygame.draw.rect(screen, self.color, self.rect)
		pygame.draw.rect(screen, self.color, self.head_rect)

pipes = [ Pipe(position) for position in ["top", "bottom"] ]


def main():
	while True:

		screen.fill(Settings.screen_bg_color)

		Bird.show()
		Bird.move()

		for pipe in pipes:
			pipe.show()
			pipe.move()
			if pipe.rect.right <= 0:
				pipes[0].rect.topleft = screen_rect.topright
				pipes[1].rect.bottomleft = screen_rect.bottomright

				random_height = choice([0, 25, 50, 75, 100, 125, 150])
				minimum_height = land.rect.height + (0.1*screen_rect.height)
				new_height_bottom = minimum_height + random_height
				new_height_top = screen_rect.height - new_height_bottom - screen_rect.height//5

				pipes[1].rect = pygame.Rect(0, 0, 0.15*screen_rect.width, new_height_bottom)
				pipes[0].rect = pygame.Rect(0, 0, 0.15*screen_rect.width, new_height_top)

				pipes[1].rect.bottomleft = screen_rect.bottomright
				pipes[0].rect.topleft = screen_rect.topright
				#print(pipes[0].rect.height, pipes[1].rect.height)

		land.show()
		land.move()



		pygame.time.Clock().tick(Settings.fps)
		pygame.display.flip()

		for every_event in pygame.event.get():
			if every_event.type == pygame.QUIT:
				pygame.quit()

			elif every_event.type == pygame.KEYDOWN:
				if every_event.key == pygame.K_SPACE:
					Bird.fly = True

			elif every_event.type == pygame.KEYUP:	
				if every_event.key == pygame.K_SPACE:
					Bird.fly = False

			elif every_event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()

class Game():

	pygame.init()
	settings = Settings()

	screen = pygame.display.set_mode(self.settings.screen_size)
	screen_rect = self.screen.get_rect()

	land = Land(self)
	bird = Bird(self)

if __name__ == '__main__':
	main()