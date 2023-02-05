import pygame
from variables import LAVA_IMG, TILE_SIZE


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(LAVA_IMG, (TILE_SIZE, TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
