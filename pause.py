#the statup for the pause stuff
import pygame, os, sys, save, player, menu
size = width, height = 672, 378
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bar = player.bar()

#the main menu button
def mainMenu(mousePosition,mouseClick):
	mainmenu1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Mainmenu1.png')).convert_alpha())
	mainmenu2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Mainmenu2.png')).convert_alpha())
	mainmenuRect = pygame.rect.Rect(116*2,  121*2, 100*2, 36*2)
	if mainmenuRect.collidepoint(mousePosition):
		screen.blit(mainmenu2, mainmenuRect)
		pygame.display.update(mainmenuRect)
		if mouseClick[0] == True:
			pygame.mixer.music.load(os.path.join('Music' '\\' 'main.mp3'))
			pygame.mixer.music.play(-1, 0.0)
			running = False
			menu.run()
			print("muneed")
	else:
		screen.blit(mainmenu1, mainmenuRect)
		pygame.display.update(mainmenuRect)
#the main options button
def options(mousePosition,mouseClick):
	options1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Options1.png')).convert_alpha())
	options2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Options2.png')).convert_alpha())
	optionsRect = pygame.rect.Rect(116*2,  85*2, 100*2, 36*2)
	if optionsRect.collidepoint(mousePosition):
		screen.blit(options2, optionsRect)
		pygame.display.update(optionsRect)
		if mouseClick[0] == True:
			print("optionised")
	else:
		screen.blit(options1, optionsRect)
		pygame.display.update(optionsRect)
#the main resume button
def resume(mousePosition,mouseClick):
	global running
	resume1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Resume1.png')).convert_alpha())
	resume2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Resume2.png')).convert_alpha())
	resumeRect = pygame.rect.Rect(116*2,  13*2, 100*2, 36*2)
	if resumeRect.collidepoint(mousePosition):
		screen.blit(resume2, resumeRect)
		pygame.display.update(resumeRect)
		if mouseClick[0] == True:
			running = False
			print("resumed!")
	else:
		screen.blit(resume1, resumeRect)
		pygame.display.update(resumeRect)
#this saves the game whilst in the pause menu
def Save(mousePosition,mouseClick):
	save1 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Save1.png')).convert_alpha())
	save2 = pygame.transform.scale2x(pygame.image.load(os.path.join('UI' + '\\' + 'Pausemenu' + '\\' + 'Save2.png')).convert_alpha())
	saveRect = pygame.rect.Rect(116*2,  49*2, 100*2, 36*2)
	global running
	if saveRect.collidepoint(mousePosition):
		screen.blit(save2, saveRect)
		pygame.display.update(saveRect)
		if mouseClick[0] == True:
			running = False
			save.quicksave(player.map.rect.x, player.map.rect.y, bar.manavalue, bar.manamax, bar.hp, bar.healthmax)
			print("saved")
	else:
		screen.blit(save1, saveRect)
		pygame.display.update(saveRect)
#main loop for the pause menu
def run():
	global running
	running = True
	while running == True:
		mouseClick = pygame.mouse.get_pressed()
		mousePosition = pygame.mouse.get_pos()
		pressed = pygame.key.get_pressed()
		if pressed == pygame.K_ESCAPE:
			running = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running =  False
		mainMenu(mousePosition,mouseClick)
		options(mousePosition,mouseClick)
		resume(mousePosition,mouseClick)
		Save(mousePosition,mouseClick)
		clock.tick(60)