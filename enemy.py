#Enemy Module, I have no idea what the hell im supposed to do, but... Lets get to work!
import pygame, os, random, player, math, game, io
size = width, height = 672, 378
screen = pygame.display.set_mode(size)
class enemy(pygame.sprite.Sprite):
	def __init__(self, character):
		pygame.sprite.Sprite.__init__(self)
		self.animationState = ['right', 'left', 'up', 'down']
		self.character = character
		randomDirection = random.randrange(0, 4)
		self.map = pygame.image.load('map.png').convert_alpha()
		self.maprect = self.map.get_rect()
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + self.animationState[randomDirection] + '.png')).convert_alpha(), (39, 51))
		self.rect = self.image.get_rect()
		self.location = random.randrange(self.maprect[0], self.maprect[2]), random.randrange(self.maprect[1], self.maprect[3])
		self.rect.topleft = self.location
	def moveRight(self):
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'Right.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'RightOne.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'RightTwo.png')).convert_alpha(), (39, 51))
	def moveLeft(self):
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'Left.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'LeftOne.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'LeftTwo.png')).convert_alpha(), (39, 51))
	def moveUp(self):
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'Up.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'UpOne.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'UpTwo.png')).convert_alpha(), (39, 51))
	def moveDown(self):
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'Down.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'DownOne.png')).convert_alpha(), (39, 51))
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'Enemies' + '\\', self.character + 'DownTwo.png')).convert_alpha(), (39, 51))
	def generateNodeList(self):
		#Node = 24x18
		nodeList = []
		for j in range(0, 21):    #height
			for i in range(0,28): #length
				a = pygame.rect.Rect(i*24, j*18, 24, 18)
				nodeList.append(a)
		return nodeList
	def makeGrid(self):
		self.grid = pygame.image.load('grid.png')
		for i in range(len(self.generateNodeList())):
			screen.blit(self.grid, self.generateNodeList()[i])
	def createVector(self):
		self.origin = [game.chr.rect.x, game.chr.rect.y]
		self.enemy = [self.rect.x, self.rect.y]
		self.a = self.origin[0] - self.enemy[0]
		self.b = self.origin[1] - self.enemy[1]
		self.c = math.sqrt(self.a**2 + self.b**2)
		self.angle = math.degrees(math.atan(self.a/self.b))
	def update(self):
		self.rect = self.image.get_rect()
		screen.blit(self.image, self.rect)