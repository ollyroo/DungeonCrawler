import pygame
screen = pygame.display.set_mode((672, 378))
class textBox(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale2x(pygame.image.load('textBox.png').convert_alpha())
		self.rect = self.image.get_rect()
		self.rect.topleft = 84, 234
		self.font = pygame.font.Font('freesansbold.ttf', 13)
	def blit(self):
		screen.blit(self.image, self.rect)
	def split(self, text):
		self.text = list(text)
	def convertLines(self):
		self.line = ''.join(self.text[:77])
		self.linerect = self.rect
		self.linerect.topleft = self.linerect[0] + 10, self.linerect[1] + 10
		print (self.line)
		self.text = self.font.render(self.line, 1, (255,255,255))
	def blitLines(self):
		screen.blit(self.text, self.rect)
	def run(self, text):
		self.blit()
		self.split(text)
		self.convertLines()
		self.blitLines()