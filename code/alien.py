import pygame 


class Alien(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		super.__init__()
		self.image = pygame.image.load('../graphics/' + color + '.png')
		self.rect = self.image.get_rect(topleft=(x,y))
		if color == 'red': value = 100
		elif color == 'green': self.value = 200
		else: self.value = 300


	def update(self, direction):
		self.rect.x += direction
		