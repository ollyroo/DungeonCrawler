import pygame, os, io, sys, math, enemy, linecache
screen = pygame.display.set_mode((672, 378))
map = pygame.sprite.Sprite()
map.image = pygame.image.load('map.png').convert_alpha()
map.rect = map.image.get_rect()
savefile = io.open(os.path.join('saves' + '\\' + 'savefile.txt'), 'r')
x = savefile.__next__()
y = savefile.__next__()
map.rect.topleft = (int(x), int(y))
map.mask = pygame.mask.from_surface(map.image)
print(map.mask.count())
ui = pygame.transform.scale2x(pygame.image.load('UI.png').convert_alpha())
savefile.close()
font = pygame.font.Font('font.ttf', 15)
enemy = enemy.enemy('whiteWolf')
class character(pygame.sprite.Sprite):
	def __init__(self, character):
		pygame.sprite.Sprite.__init__(self)
		self.character = character
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'Down.png')).convert_alpha(), (39, 51))
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image, 127)
		self.rect.topleft = 336 - self.rect[2], 189 - self.rect[3]
		self.direction = None
	def moveRight(self):
		if self.direction != 'right':
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'Right.png')).convert_alpha(), (39, 51))
			self.directionType = 0
			self.direction = 'right'
		elif self.directionType == 0:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'RightOne.png')).convert_alpha(), (39, 51))
		elif self.directionType == 15:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'RightTwo.png')).convert_alpha(), (39, 51))
			self.directionType = -15
		self.directionType += 1
	def moveLeft(self):
		if self.direction != 'left':
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'Left.png')).convert_alpha(), (39, 51))
			self.directionType = 0
			self.direction = 'left'
		elif self.directionType == 0:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'LeftOne.png')).convert_alpha(), (39, 51))
		elif self.directionType == 15:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'LeftTwo.png')).convert_alpha(), (39, 51))
			self.directionType = -15
		self.directionType += 1
	def moveUp(self):
		if self.direction != 'up':
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'Up.png')).convert_alpha(), (39, 51))
			self.directionType = 0
			self.direction = 'up'
		elif self.directionType == 0:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'UpOne.png')).convert_alpha(), (39, 51))
		elif self.directionType == 15:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'UpTwo.png')).convert_alpha(), (39, 51))
			self.directionType = -15
		self.directionType += 1
	def moveDown(self):
		if self.direction != 'down':
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'Down.png')).convert_alpha(), (39, 51))
			self.directionType = 0
			self.direction = 'down'
		elif self.directionType == 0:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'DownOne.png')).convert_alpha(), (39, 51))
		elif self.directionType == 15:
			self.image = pygame.transform.scale(pygame.image.load(os.path.join("characters" + '\\' + 'playable' + '\\', self.character + 'DownTwo.png')).convert_alpha(), (39, 51))
			self.directionType = -15
		self.directionType += 1
	def movement(self, pressed):
		if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
			self.moveLeft()
			map.rect.x += 22
			if map.mask.get_at((self.rect.x - map.rect.x, self.rect.y - map.rect.y)) == 0 or map.mask.get_at(((self.rect.x) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), self.rect.y - map.rect.y)) == 0:
				map.rect.x -= 22
				print('collision')
			else:
				map.rect.x -= 20
		elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
			self.moveRight()
			map.rect.x -= 22
			if map.mask.get_at((self.rect.x - map.rect.x, self.rect.y - map.rect.y)) == 0 or map.mask.get_at(((self.rect.x) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), self.rect.y - map.rect.y)) == 0:
				map.rect.x += 22
				print('collision')
			else:
				map.rect.x += 20
		elif pressed[pygame.K_w] or pressed[pygame.K_UP]:
			self.moveUp()
			map.rect.y += 15
			if map.mask.get_at((self.rect.x - map.rect.x, self.rect.y - map.rect.y)) == 0 or map.mask.get_at(((self.rect.x) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), self.rect.y - map.rect.y)) == 0:
				map.rect.y -= 15
				print('collision')
			else:
				map.rect.y -= 13
		elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
			self.moveDown()
			map.rect.y -= 15
			if map.mask.get_at((self.rect.x - map.rect.x, self.rect.y - map.rect.y)) == 0 or map.mask.get_at(((self.rect.x) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))) == 0 or map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), self.rect.y - map.rect.y)) == 0:
				map.rect.y += 15
				print('collision', map.mask.get_at((self.rect.x - map.rect.x, self.rect.y - map.rect.y)), map.mask.get_at(((self.rect.x) - (map.rect.x), (map.rect.y + map.rect.h) - (self.rect.y + self.rect.h))), map.mask.get_at(((self.rect.x + self.rect.w) - (map.rect.x), self.rect.y - map.rect.y)))
			else:
				map.rect.y += 13
	def update(self, pressed):
		self.movement(pressed)
		screen.fill((220,220,220))
		screen.blit(map.image, map.rect)
		screen.blit(self.image, self.rect)
		screen.blit(ui, (0,0))
class bar():
	def __init__(self):
		self.healthimage = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'HUD' +  '\\' + 'HP.png')))
		self.healthrect = self.healthimage.get_rect()
		self.healthrect.topleft = 82, 155*2
		self.healthbackup = self.healthrect[2]
		self.healthmax = int(linecache.getline(os.path.join('saves' + '\\' + 'savefile.txt'), 5))
		self.hp = self.healthmax
		self.healthvar = int(linecache.getline(os.path.join('saves' + '\\' + 'savefile.txt'), 4))
		self.manaimage = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'HUD' +  '\\' + 'mana.png')))
		self.manarect = self.manaimage.get_rect()
		self.manarect.topleft = 180*2, 155*2
		self.manabackup = self.manarect[2]
		self.manamax = int(linecache.getline(os.path.join('saves' + '\\' + 'savefile.txt'), 8))
		self.manavalue = self.manamax
		self.manavar = int(linecache.getline(os.path.join('saves' + '\\' + 'savefile.txt'), 7))
		if self.manavar < self.manamax:
			self.modify('mana', 'subtract', self.manamax - self.manavar)
		if self.healthvar < self.healthmax:
			self.modify('health', 'subtract', self.healthmax - self.healthvar)
	def modify(self, type, operation, value):
		self.healthimage = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'HUD' +  '\\' + 'HP.png')))
		self.manaimage = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'HUD' +  '\\' + 'mana.png')))
		if operation == 'add':
			if type == 'mana':
				self.manavalue += value
				if self.manavalue > self.manamax:
					self.manavalue = self.manamax
			if type == 'health':
				self.hp += value
				if self.hp > self.healthmax:
					self.hp = self.healthmax
		if operation == 'subtract':
			if type == 'mana':
				self.manavalue -= value
				if self.manavalue < 0:
					self.manavalue = 0
			if type == 'health':
				self.hp -= value
				if self.hp < 0:
					self.hp = 0
		self.manaAlgorithm = math.ceil(self.manavalue/self.manamax*self.manabackup)
		self.healthAlgorithm = math.ceil(self.hp/self.healthmax*self.healthbackup)
		self.manaimage = pygame.transform.scale(self.manaimage, (self.manarect[2] - (self.manarect[2] - self.manaAlgorithm), self.manarect[3]))
		self.healthimage = pygame.transform.scale(self.healthimage, (self.healthrect[2] - (self.healthrect[2] - self.healthAlgorithm), self.healthrect[3]))
		self.manarect = self.manaimage.get_rect()
		self.healthrect = self.healthimage.get_rect()
		self.manarect.topleft = 180*2, 155*2
		self.healthrect.topleft = 82, 155*2
		if self.manavalue == 0:
			print ("You're Out of Mana")
		if self.hp == 0:
			print('You are dead')
	def text(self):
		self.manastring = font.render(str(self.manavalue) + "\\" + str(self.manamax), 1, (255,255,255))
		self.manacoords = 180*2, 146*2
		self.healthstring = font.render(str(self.hp) + "\\" + str(self.healthmax), 1, (255,255,255))
		self.healthcoords = 41*2, 146*2
	def update(self):
		self.text()
		screen.blit(self.manaimage, self.manarect)
		screen.blit(self.manastring, self.manacoords)
		screen.blit(self.healthimage, self.healthrect)
		screen.blit(self.healthstring, self.healthcoords)
class hotBar():
	def __init__(self):
		self.zero = pygame.rect.Rect(273*2, 161*2, 22*2, 22*2)
		self.one = pygame.rect.Rect(41*2, 161*2, 22*2, 22*2)
		self.two = pygame.rect.Rect(64*2, 161*2, 22*2, 22*2)
		self.three = pygame.rect.Rect(87*2, 161*2, 22*2, 22*2)
		self.four = pygame.rect.Rect(110*2, 161*2, 22*2, 22*2)
		self.five = pygame.rect.Rect(133*2, 161*2, 22*2, 22*2)
		self.six = pygame.rect.Rect(181*2, 161*2, 22*2, 22*2)
		self.seven = pygame.rect.Rect(204*2, 161*2, 22*2, 22*2)
		self.eight = pygame.rect.Rect(227*2, 161*2, 22*2, 22*2)
		self.nine = pygame.rect.Rect(250*2, 161*2, 22*2, 22*2)
	def mouseCollision(self, rect, mousePosition):
		if rect.collidepoint(mousePosition):
			return True
	def update(self, mousePosition, rect, mouseClick, pressed, key, function):
		if self.mouseCollision(rect, mousePosition) and mouseClick[0] == True or pressed[key] == True:
			function()
			print ('You pressed', chr(key))
class bag():
	def __init__(self):
		self.rect = pygame.rect.Rect(314, 310, 44, 54)
		self.inventoryImage = pygame.transform.scale2x(pygame.image.load('inventory.png').convert_alpha())
		self.inventoryRect = self.inventoryImage.get_rect()
		self.inventoryRect.topleft = 172, 57
		self.open = False
	def mouseCollision(self, rect, mousePosition):
		if rect.collidepoint(mousePosition):
			return True
	def update(self, mousePosition, mouseClick, pressed):
		if self.mouseCollision(self.rect, mousePosition) and mouseClick[0] == True or pressed[pygame.K_i] == True:
			if self.open == True:
				self.open = False
			elif self.open == False:
				self.open = True
		if self.open == True:
			screen.blit(self.inventoryImage, self.inventoryRect)