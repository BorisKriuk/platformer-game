import pygame
from variables import COIN_IMG, TILE_SIZE


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(COIN_IMG, (TILE_SIZE // 2, TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
