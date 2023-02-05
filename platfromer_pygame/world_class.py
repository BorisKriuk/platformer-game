import pygame
from enemy_class import Enemy
from lava_class import Lava
from exit_class import Exit
from coin_class import Coin
from platform_class import Platform
from variables import DIRT_IMG, GRASS_IMG, TILE_SIZE


class World:
    def __init__(self, data, screen, blob_group, lava_group, exit_group, coin_group, platform_group):
        self.tile_list = []
        self.screen = screen
        self.blob_group = blob_group
        self.lava_group = lava_group
        self.exit_group = exit_group
        self.coin_group = coin_group
        self.platform_group = platform_group

        for row_count, row in enumerate(data):
            for col_count, tile in enumerate(row):
                if tile == 1:
                    img = pygame.transform.scale(DIRT_IMG, (TILE_SIZE, TILE_SIZE))

                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE

                    self.tile_list.append((img, img_rect))

                if tile == 2:
                    img = pygame.transform.scale(GRASS_IMG, (TILE_SIZE, TILE_SIZE))

                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE

                    self.tile_list.append((img, img_rect))

                if tile == 3:
                    blob = Enemy(col_count*TILE_SIZE, row_count*TILE_SIZE+15)
                    self.blob_group.add(blob)

                if tile == 6:
                    lava = Lava(col_count*TILE_SIZE, row_count*TILE_SIZE + TILE_SIZE // 2)
                    self.lava_group.add(lava)

                if tile == 8:
                    exit_var = Exit(col_count*TILE_SIZE, row_count*TILE_SIZE - TILE_SIZE // 2)
                    self.exit_group.add(exit_var)

                if tile == 7:
                    coin = Coin(col_count * TILE_SIZE + TILE_SIZE // 2, row_count * TILE_SIZE + TILE_SIZE // 2)
                    self.coin_group.add(coin)

                if tile == 4:
                    platform = Platform(col_count * TILE_SIZE, row_count * TILE_SIZE, 1, 0)
                    self.platform_group.add(platform)

                if tile == 5:
                    platform = Platform(col_count * TILE_SIZE, row_count * TILE_SIZE, 0, 1)
                    self.platform_group.add(platform)

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
