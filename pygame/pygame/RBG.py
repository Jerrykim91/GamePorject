import pygame
# import
# 여러가지 색
# 0-255 ( R, B, G )
# 0-255 ( R, B, G )
RED   = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
BLUE  = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127   # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0        # 검은색: 적   0, 녹   0, 청   0
GRAY  = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE   = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255
SILVER  = 204, 204, 204 # 은색  : 적 204, 녹 204, 청 204
BBARRY  = 204, 204, 255
#DPGREEN = 000, 050, 000
PINK   = 255, 204, 204
PEACH  = 255, 153, 153
#DPBLUE = 000, 051, 153
YELLOW = 255, 255, 000
HEXGRAY = 102, 102, 102

# 게임 데이터
WIDTH  = 10
HEIGHT = 10
MARGIN = 1
WINDOW_SIZE_W = 600
WINDOW_SIZE_H = 500
RES_PATH = './data/'
# BG_IMG = 'img_B0.png'
BG_IMG = 'new1116.png'
WINDOW_CAPTION = 'Room5'

import pygame
# AGV의 방향 상수값
# DIRECTION_ON_KEY = {
#     pygame.K_UP    : 'north',
#     pygame.K_DOWN  : 'south',
#     pygame.K_LEFT  : 'west',
#     pygame.K_RIGHT : 'east'
# }
DIR_N = 1
DIR_S = 2
DIR_W = 3
DIR_E = 4