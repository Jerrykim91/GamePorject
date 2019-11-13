import pygame, sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
from RBG import *
# from elements import *

# unload : 0  , load = 1 , caner = 2 , turn = 3
# home_ in : 4  , home_out : 5 , home point = 9
# M_in : 6  , M _out : 7
# check point1 = 8

pygame.init()

WIDTH = 5
HEIGHT = 5
MARGIN = 1
x = 0
y = 0
# -----
WINDOW_SIZE = [600, 500]
Win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Room1")
clock = pygame.time.Clock()
# -----

data = pd.read_csv('./data/site3.csv')

Win.fill(WHITE)

for i in range(data.shape[0]):  # 500 = i = row
    for j in range(data.shape[1]):  # 600
        if data.iloc[i, j] == 1:
            Color = BLACK
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 4:
            Color = GREEN
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 5:
            Color = RED
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        else:
            Color = WHITE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))


done = False
# -------- 메인 프로그램 루프 -----------
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True


    clock.tick(60)
    pygame.display.flip()

pygame.quit()
