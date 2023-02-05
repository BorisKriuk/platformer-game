import pygame
from variables import DEAD_IMG, BLUE, SCREEN_WIDTH, SCREEN_HEIGHT, JUMP_FX, GAME_OVER_FX


class Player:
    def __init__(self, x, y, screen, world, blob_group, lava_group, exit_group, platform_group):
        self.reset(x, y, screen, world, blob_group, lava_group, exit_group, platform_group)

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        if self.game_over == 0:

            # get key presses
            key = pygame.key.get_pressed()

            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                JUMP_FX.play()
                self.vel_y -= 25
                self.jumped = True

            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            self.in_air = True
            for tile in self.world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                    dx = 0

                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0

                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # check for collision with enemies
            if pygame.sprite.spritecollide(self, self.blob_group, False):
                self.game_over = -1
                GAME_OVER_FX.play()

            # check for collision with lava
            if pygame.sprite.spritecollide(self, self.lava_group, False):
                self.game_over = -1
                GAME_OVER_FX.play()

            # check for collision with exit
            if pygame.sprite.spritecollide(self, self.exit_group, False):
                self.game_over = 1

            # check for collision with platforms
            for platform in self.platform_group:
                # collision in the x direction
                if platform.rect.colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                    dx = 0
                # collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    # check if below the platform
                    if abs((self.rect.top+dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    # check if above the platform
                    elif abs((self.rect.bottom+dy)-platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    # move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction


            # update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif self.game_over == (-1):
            self.image = self.dead_image

            font = pygame.font.SysFont('Bauhaus 93', 70)
            img = font.render("GAME OVER!", True, BLUE)
            self.screen.blit(img, ((SCREEN_WIDTH // 2) - 120, SCREEN_HEIGHT // 2))

            if self.rect.y >= 200:
                self.rect.y -= 5

        # draw a player onto screen
        self.screen.blit(self.image, self.rect)

        return self.game_over

    def reset(self, x, y, screen, world, blob_group, lava_group, exit_group, platform_group):
        self.screen = screen
        self.world = world
        self.blob_group = blob_group
        self.lava_group = lava_group
        self.exit_group = exit_group
        self.platform_group = platform_group
        self.game_over = 0

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.dead_image = DEAD_IMG
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
