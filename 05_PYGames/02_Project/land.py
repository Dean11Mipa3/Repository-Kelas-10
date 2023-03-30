import pygame

class Land():

	def __init__(self):
		self.settings = game.settings
		self.screen = game.screen
		self.screen.rect = game.screen_rect

		self.image = pygame.transform.scale(pygame.image.load("images/land.png"), (2*screen_rect.width, screen_rect.height//5))
		self.rect = self.image.get_rect()

		self.rect.midbottom = screen_rect.midbottom

	def move(self):
		self.rect.x -= Settings.land_speed
		if self.rect.centerx <= 0:
			self.rect.left = screen_rect.left

	def show(self):
		self.screen.blit(self.image, self.rect)
