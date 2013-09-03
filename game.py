import pygame
from pygame.locals import *
import sys, text, save, player, minimap, enemy, math, pause
enemy = enemy.enemy('whiteWolf')
clock = pygame.time.Clock()
background = pygame.transform.scale2x(pygame.image.load('UI.png').convert_alpha())
pygame.init()
pygame.display.set_caption('Dungeon Crawler')
pygame.display.set_icon(pygame.image.load('icon.png'))
size = width, height = 672, 378
screen = pygame.display.set_mode(size)
screen.blit(background, (0,0))
pygame.display.update()
chr = player.character("cleric")
textBox = text.textBox()
hotbar = player.hotBar()
bag = player.bag()
bar = player.bar()
regen = False
exit = False
nodeScreen = False
def nothing():
	pass
def hotbarUpdate():
	hotbar.update(mousePosition, hotbar.zero, mouseClick, pressed, pygame.K_0, nothing)
	hotbar.update(mousePosition, hotbar.one, mouseClick, pressed, pygame.K_1, nothing)
	hotbar.update(mousePosition, hotbar.two, mouseClick, pressed, pygame.K_2, nothing)
	hotbar.update(mousePosition, hotbar.three, mouseClick, pressed, pygame.K_3, nothing)
	hotbar.update(mousePosition, hotbar.four, mouseClick, pressed, pygame.K_4, nothing)
	hotbar.update(mousePosition, hotbar.five, mouseClick, pressed, pygame.K_5, nothing)
	hotbar.update(mousePosition, hotbar.six, mouseClick, pressed, pygame.K_6, nothing)
	hotbar.update(mousePosition, hotbar.seven, mouseClick, pressed, pygame.K_7, nothing)
	hotbar.update(mousePosition, hotbar.eight, mouseClick, pressed, pygame.K_8, nothing)
	hotbar.update(mousePosition, hotbar.nine, mouseClick, pressed, pygame.K_9, nothing)
def debug():
	font =pygame.font.Font('freesansbold.ttf', 13)
	fps = font.render('FPS = ' + str(math.ceil(clock.get_fps())), 1, (255,255,255))
	screen.blit(fps, (0,0))
def run():
	global mousePosition, mouseClick, pressed, regen
	debugScreen = False
	exit = False
	nodeScreen = False
	while True:
		pressed = pygame.key.get_pressed()
		mouseClick = pygame.mouse.get_pressed()
		mousePosition = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause.run()
				if event.key == K_F3:
					if debugScreen == True:
						debugScreen = False
					elif debugScreen == False:
						debugScreen = True
				if event.key == K_BACKQUOTE:
					function = input()
					eval(function)
				if event.key == K_F5:
					print("crappy code imbound")
					nodeScreen = True
			bag.update(mousePosition, mouseClick, pressed)
			hotbarUpdate()
		if bag.open == False:
			pygame.display.flip()
			chr.update(pressed)
			enemy.update()
			minimap.update()
		if bag.open == True:
			pygame.display.update(bag.inventoryRect)
		if debugScreen == True:
			debug()
		if nodeScreen == True:
			enemy.makeGrid()
			pygame.display.flip()
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == K_F5:
							exit = True
				if exit == True:
					nodeScreen = False
					exit = False
					break
				
		bar.update()
		clock.tick(60)
