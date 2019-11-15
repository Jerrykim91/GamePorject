# import
import pygame, sys
import numpy as np
import random
import pandas as pd
from pygame.locals import QUIT, KEYDOWN
from RBG import *

pygame.init()

#데이터 불러오기
data = pd.read_csv('./data/site3.0.csv')
# print(data)

WINDOW_SIZE = (600, 500)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

BLOCK_SIZE = 10
MARGIN = 1
WIDTH = 10
HEIGHT = 10
vel = 1

img = pygame.image.load('./data/img_B0.png')
screen = pygame.display.set_mode(WINDOW_SIZE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Room2")

# positions = []
# for i in range(data.shape[0]):
#     for j in range(data.shape[1]):
#         positions = data.iloc[i][j]
#         if positions == 1:
#             print("happy")
#         elif positions == 0:
#             print("0")
#         else:
#


for i in range(data.shape[0]):  # 500 = i = row
    for j in range(data.shape[1]):  # 600
        # print(data.iloc[i, j])
        if data.iloc[i, j] == 1:
            Color = BLACK
            pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 2:
            Color = GREEN
            pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 3:
            Color = RED
            pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 4:
            Color = GREEN
            pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 5:
            Color = RED
            pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        # elif data.iloc[i, j] == 6:
        #     # Color = GREEN
        #     # pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        # elif data.iloc[i, j] == 7:
        #     # Color = RED
        #     # pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        # elif data.iloc[i, j] == 8:
        #     # Color = RED
        #     # pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        else:
            Color = WHITE
            pygame.draw.rect(screen, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))

    # unload : 0  , load = 1 ,  = 2 ,  = 3
    # home_ in : 4  , home_out : 5 , home point = 9
    # M_in : 6  , M _out : 7
    # M = 8


# ======= 함수 =======
def draw_background(screen):
    """ 게임의 배경을 그린다. """
    # 화면 배경 설정
    #screen.fill(WHITE)
    screen.blit(img, (0, 0))
    #pygame.image.load('./data/img_B0.png')
    for row in range(60):
        pygame.draw.line(screen, (64, 64, 64), (row * 10, 0), (row * 10, 600))
        pygame.draw.line(screen, (64, 64, 64), (0, row * 10), (600, row * 10))


def draw_block(screen, color, position):
    """ position 위치에 color 블록을 그린다. """
    block = pygame.Rect((position[1] * WIDTH+MARGIN, position[0] * HEIGHT+MARGIN), (WIDTH, HEIGHT))
    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect(screen, color, block)

# ==== 변수 ======
block_position = [0,0]
Run = True

# -------- main loop --------
while Run:
    CLOCK.tick(27)
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            Run = False

        if event.type == pygame.KEYDOWN:
            pos = pygame.key.get_pressed()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            if event.key == pygame.K_LEFT : #block_position[1]
                block_position[1] -= vel
            elif event.key == pygame.K_RIGHT:
                block_position[1] += vel
            elif event.key == pygame.K_UP :
                block_position[0] -= vel #block_position[0]
            elif event.key == pygame.K_DOWN :
                block_position[0] += vel

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, RED, block_position)
    pygame.display.flip()

pygame.quit()


# DIRECTION_ON_KEY = {
#     pygame.K_UP : 'north',
#     pygame.K_DOWN : 'south',
#     pygame.K_LEFT : 'west',
#     pygame.K_RIGHT : 'east'
# }