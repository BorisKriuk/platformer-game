import pygame
from variables import PLATFORM_IMG, TILE_SIZE


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(PLATFORM_IMG, (TILE_SIZE, TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y

        self.move_counter += 1
        if self.move_counter > 50:
            self.move_direction *= (-1)
            self.move_counter *= (-1)
