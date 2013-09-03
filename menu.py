import pygame, sys, os
pygame.init()
pygame.display.set_caption('Dungeon Crawler')
pygame.display.set_icon(pygame.image.load('icon.png'))
size = width, height = 672, 378
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mixer.music.load(os.path.join('Music' '\\' 'main.mp3'))
pygame.mixer.music.play(-1, 0.0)

def newGame():
	newState1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'newState1.png')).convert_alpha())
	newState2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'newState2.png')).convert_alpha())
	newRect = pygame.rect.Rect(34*2,  114*2, 100*2, 36*2)
	if newRect.collidepoint(mousePosition):
		screen.blit(newState2, newRect)
		pygame.display.update(newRect)
		if mouseClick[0] == True:
			pygame.mixer.music.load(os.path.join('Music' '\\' 'FINAL_2.wav'))
			pygame.mixer.music.play(-1, 0.0)
			import save
			save.newgame()
			import game
			game.run()
	else:
		screen.blit(newState1, newRect)
		pygame.display.update(newRect)
def loadGame():
	loadState1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'loadState1.png')).convert_alpha())
	loadState2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'loadState2.png')).convert_alpha())
	loadRect = pygame.rect.Rect(34*2, 74*2, 100*2, 36*2)
	if loadRect.collidepoint(mousePosition):
		screen.blit(loadState2, loadRect)
		pygame.display.update(loadRect)
		if mouseClick[0] == True:
			if os.path.exists(os.path.join('saves' + '\\' + 'savefile.txt')) == False:
				pass
			else:
				pygame.mixer.music.load(os.path.join('Music' '\\' 'FINAL_2.wav'))
				pygame.mixer.music.play(-1, 0.0)
				import game
				game.run()
	else:
		screen.blit(loadState1, loadRect)
		pygame.display.update(loadRect)
		
def options():
	optionsState1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'optionsState1.png')).convert_alpha())
	optionsState2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'optionsState2.png')).convert_alpha())
	optionsRect = pygame.rect.Rect(210*2, 74*2, 100*2, 36*2)
	if optionsRect.collidepoint(mousePosition):
		screen.blit(optionsState2, optionsRect)
		pygame.display.update(optionsRect)
	else:
		screen.blit(optionsState1, optionsRect)
		pygame.display.update(optionsRect)

def exit():
	exitState1 =pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'exitState1.png')).convert_alpha())
	exitState2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'exitState2.png')).convert_alpha())
	exitRect = pygame.rect.Rect(210*2, 114*2, 100*2, 36*2)
	if exitRect.collidepoint(mousePosition):
		screen.blit(exitState2, exitRect)
		pygame.display.update(exitRect)
		if mouseClick[0] == True:
			sys.exit()
	else:
		screen.blit(exitState1, exitRect)
		pygame.display.update(exitRect)
def run():
	global mousePosition, mouseClick
	currentOptions = ['new game', 'options', 'load game', 'exit']
	background = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'main menu' + '\\' + 'menu.png')).convert_alpha())
	screen.blit(background, (0,0))
	pygame.display.update()
	while True:
		pressed = pygame.key.get_pressed()
		mouseClick = pygame.mouse.get_pressed()
		mousePosition = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
			loadGame()
			options()
			newGame()
			exit()
			clock.tick(60)