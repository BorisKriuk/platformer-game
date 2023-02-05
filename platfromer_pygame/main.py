import pygame
import pickle
from os import path
from variables import SCREEN_WIDTH, SCREEN_HEIGHT, SUN_IMG, BG_IMG, RESTART_IMG, START_IMG, \
    EXIT_IMG, MAX_LEVEL, WHITE, BLUE, TILE_SIZE, COIN_FX
from world_class import World
from player_class import Player
from button_class import Button
from coin_class import Coin


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function to reset level
def reset_level(level):
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()
    platform_group.empty()
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
        world = World(world_data, screen, blob_group, lava_group, exit_group, coin_group, platform_group)
        player.reset(100, SCREEN_HEIGHT - 130, screen, world, blob_group, lava_group, exit_group, platform_group)

        return world


pygame.init()

clock = pygame.time.Clock()
fps = 60

game_over = 0
main_menu = True
level = 0
score = 0
font_score = pygame.font.SysFont('Bauhaus 93', 34)
font = pygame.font.SysFont('Bauhaus 93', 70)

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer 1.0")

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()

# create dummy coin for showing the score
score_coin = Coin(TILE_SIZE // 2, TILE_SIZE // 2)
coin_group.add(score_coin)

# load in level data and create world for the player
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)

    world = World(world_data, screen, blob_group, lava_group, exit_group, coin_group, platform_group)
    player = Player(100, SCREEN_HEIGHT - 130, screen, world, blob_group, lava_group, exit_group, platform_group)

# create buttons
restart_button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100, RESTART_IMG, screen)
start_button = Button(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2, START_IMG, screen)
exit_button = Button(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2, EXIT_IMG, screen)

running = True
while running:
    print(score)
    clock.tick(fps)

    screen.blit(BG_IMG, (0, 0))
    screen.blit(SUN_IMG, (100, 100))

    if main_menu:
        if exit_button.draw():
            running = False
        if start_button.draw():
            main_menu = False
    else:

        world.draw()

        if game_over == 0:
            blob_group.update()
            platform_group.update()
            # update score
            # check if the coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                COIN_FX.play()
            draw_text("X " + str(score), font_score, WHITE, TILE_SIZE - 10, 15)

        blob_group.draw(screen)

        lava_group.draw(screen)

        exit_group.draw(screen)

        coin_group.draw(screen)

        platform_group.draw(screen)

        game_over = player.update()

        # if player died
        if game_over == (-1):
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        # if player has completed the level
        if game_over == 1:
            # reset game and go to the next level
            level += 1
            if level <= MAX_LEVEL:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text("YOU WIN!", font, BLUE, (SCREEN_WIDTH // 2) - 100, SCREEN_HEIGHT // 2)
                # restart game
                if restart_button.draw():
                    level = 0
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
