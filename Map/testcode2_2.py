import pygame, sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
from RBG import *
pygame.init()

vel = 5
width, height = (8, 16)
WIDTH = 5
HEIGHT = 5
MARGIN = 1
# 좌표값
x = 0
y = 0
#-----
WINDOW_SIZE = [600, 500]
# WINDOW_SIZE = [400, 300]
Win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed")
clock = pygame.time.Clock()
path = './data/img_B0.png'
#-----
data = pd.read_csv('./data/site3.0.csv')
# data = pd.read_csv('./data/sitemin.csv')
# img = pygame.image.load( Win, path )


Win.fill(WHITE)

for i in range(data.shape[0]): # 500 = i = row
    for j in range(data.shape[1]): # 600
        if data.iloc[i, j] == 1:
            Color = BLACK
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 4:
            Color = GREEN
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 5:
            Color = RED
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 6:
            Color = BLUE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        else:
            Color = WHITE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))

# unload : 0  , load = 1 , caner = 2 , turn = 3
# home_ in : 4  , home_out : 5 , home point = 9
# M_in : 6  , M _out : 7
# check point1 = 8

done = False
# -------- 메인 프로그램 루프 -----------
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

        ##  키를 통한 방향 값 설정
    # keys = pygame.key.get_pressed()
    # # 키 입력
    # if keys[pygame.K_LEFT] and x > vel:
    #     x -= vel
    # if keys[pygame.K_RIGHT]and x < WINDOW_SIZE[0]-width-vel:
    #     x += vel
    # if keys[pygame.K_UP]and y > vel:
    #     y -= vel
    # if keys[pygame.K_DOWN]and y < WINDOW_SIZE[1]-height-vel:
    #     y += vel
    # 캐릭터 그리기
    # Win.fill((0, 0, 0))  # 잔상 없이 게임 생성
    # (win,(R,G,B),(x, y, width, height))
    # pygame.draw.rect(Win, RED, (x, y, 8, 16),3)

    clock.tick(60)
    pygame.display.flip()
    pygame.image.save(Win, path)
pygame.quit()
