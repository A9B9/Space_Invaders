import pygame 


class Obstacle(pygame.sprite.Sprite):
	def __init__(self, size: int, color: tuple, x, y):
		super().__init()
		self.image = pygame.Surface((size,size))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft=(x,y))






shape = [
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxx     xxx',
'xx       xx']