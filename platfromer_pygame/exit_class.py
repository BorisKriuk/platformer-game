import pygame
from variables import DOOR_IMG, TILE_SIZE


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(DOOR_IMG, (TILE_SIZE, int(TILE_SIZE * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y