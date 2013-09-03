import pygame, player, sys
screen = pygame.display.set_mode((672, 378))
dot = pygame.image.load('miniplayer.png').convert_alpha()
minimap = pygame.image.load('map.png').convert_alpha()
minimaprect = minimap.get_rect()
minimap = pygame.transform.scale(minimap, (int(minimaprect[2]/16), int(minimaprect[3]/16)))
minimaprect = minimap.get_rect()
gridrect = pygame.Rect(541, 2, 129, 128)
mask = pygame.transform.scale2x(pygame.image.load("minimap_mask.png").convert_alpha())


def update():
#places minimap
	full = pygame.Surface((672*2, 378*2), pygame.SRCALPHA)
	minimaprect.topleft = (int(player.map.rect.x/16) + 583, int(player.map.rect.y/16) + 53)
	full.blit(minimap, minimaprect)
	masked = full.copy()
	masked.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MULT)
	screen.blit(masked, (0, 0))

#blits the dot in the middle	
	screen.blit(dot, (602, 62))
	