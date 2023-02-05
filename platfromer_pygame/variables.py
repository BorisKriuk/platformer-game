import pygame
from pygame import mixer

# world parameters

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
TILE_SIZE = 50
MAX_LEVEL = 7

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

# load sound
COIN_FX = pygame.mixer.Sound('img_coin.wav')
COIN_FX.set_volume(0.5)

JUMP_FX = pygame.mixer.Sound('img_jump.wav')
JUMP_FX.set_volume(0.5)

GAME_OVER_FX = pygame.mixer.Sound('img_game_over.wav')
GAME_OVER_FX.set_volume(0.5)

# define font parameters

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# load images

SUN_IMG = pygame.image.load('sun.png')
BG_IMG = pygame.image.load('sky.png')
DIRT_IMG = pygame.image.load('dirt.png')
GRASS_IMG = pygame.image.load('grass.png')
GUY1_IMG = pygame.image.load('guy1.png')
ENEMY_IMG = pygame.image.load('blob.png')
LAVA_IMG = pygame.image.load('lava.png')
DEAD_IMG = pygame.image.load('ghost.png')
RESTART_IMG = pygame.image.load('restart_btn.png')
START_IMG = pygame.image.load('start_btn.png')
EXIT_IMG = pygame.image.load('exit_btn.png')
DOOR_IMG = pygame.image.load('exit.png')
COIN_IMG = pygame.image.load('coin.png')
PLATFORM_IMG = pygame.image.load('platform.png')
