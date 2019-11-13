# import
import pygame, sys
import numpy as np
import random
import pandas as pd
from pygame.locals import QUIT,KEYDOWN
from RBG import *

pygame.init()

#데이터 불러오기--------------------------
data = pd.read_csv('./data/site3.0.csv')
# print(data)

# 변수-------------------------------
WIDTH = 10
HEIGHT = 10
MARGIN = 1
WINDOW_SIZE = (600, 600)

img = pygame.image.load('./data/img_B0.png')
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Room3")

# 배열 생성------------------------------------
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        positions = data.iloc[i][j]
        if positions == 1:
            # 길위에서 캐릭터가 움직여야해
            #print("happy")
        elif positions == 0:
            #print("0")
        else:
            #print("야")

    # unload : 0  , load = 1 ,  = 2 ,  = 3
    # home_ in : 4  , home_out : 5 , home point = 9
    # M_in : 6  , M _out : 7
    # M = 8


# 배경----------------------------------
background = pygame.Rect((0, 0), (WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.draw.rect(screen, WHITE, background)



# ======= 함수 =======
def draw_background(screen):
    """ 게임의 배경을 그린다. """
    # 화면 배경 설정
    screen.blit(img, (0, 50))
    for row in range(60):
        pygame.draw.line(screen, (64, 64, 64), (row * 10, 0), (row * 10, 600))
        pygame.draw.line(screen, (64, 64, 64), (0, row * 10), (600, row * 10))

def draw_block(screen, color, position):
    """ position 위치에 color 블록을 그린다. """
    block = pygame.Rect((position[1] * WIDTH + MARGIN, position[0] * HEIGHT + MARGIN), (WIDTH, HEIGHT))
    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect(screen, color, block)

# -------- main loop --------
draw_background(screen)