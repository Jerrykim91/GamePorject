import pygame, sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
from RBG import *

pygame.init()
# colors

WIDTH = 5
HEIGHT = 5
MARGIN = 1
x = 0
y = 0
#-----
WINDOW_SIZE = [600, 500]
# WINDOW_SIZE = [400, 300]
Win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed")
clock = pygame.time.Clock()
#-----

# data = pd.read_csv('./data/site3.0.csv')
data = pd.read_csv('./data/site1115.csv')
Win.fill(WHITE)

for i in range(data.shape[0]): # 500 = i = row
    for j in range(data.shape[1]): # 600
        if data.iloc[i, j] == 1:
            Color = BLACK
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 2:
            Color = GREEN
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 8:
            Color = RED
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 4:
            Color = BLUE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 5:
            Color = GRAY
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 6:
            Color = PURPLE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        else:
            Color = WHITE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))


# unload : 0  , load = 1 ,  = 2 ,  = 3
# home_ in : 4  , home_out : 5 , home point = 9
# M_in : 6  , M _out : 7
# M = 8

done = False
# -------- 메인 프로그램 루프 -----------
while not done:
    # print(data.shape[0], data.shape[1])
    # 500, 600

            # if j == 1 :
            #     pygame.draw.rect(Win, BLACK, (int(data.columns[i]), int(data.index[j]), 1, 1))
            # elif j == 3 :
            #     pygame.draw.rect(Win, GREEN, (int(data.columns[i]), int(data.index[j]), 1, 1))
            # elif j == 4:
            #     pygame.draw.rect(Win, RED, (int(data.columns[i]), int(data.index[j]), 1, 1))
            # else :
            #     pygame.draw.rect(Win, WHITE, (int(data.columns[i]), int(data.index[j]), 1, 1))

    # for i in range(data.shape[0]) :
    #     for j in range(data.shape[1]) :
    #         if j == 1 :
    #             pygame.draw.rect(Win, BLACK, (int(data.columns[i]), int(data.index[j]), 1, 1))
    #         elif j == 3 :
    #             pygame.draw.rect(Win, GREEN, (int(data.columns[i]), int(data.index[j]), 1, 1))
    #         elif j == 4:
    #             pygame.draw.rect(Win, RED, (int(data.columns[i]), int(data.index[j]), 1, 1))
    #         else :
    #             pygame.draw.rect(Win, WHITE, (int(data.columns[i]), int(data.index[j]), 1, 1))

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    # for i in range(data.shape[0]) :
    #     for j in range(data.shape[1]) :
    #         if j == 1 :
    #             print('black')
    #             print(int(data.columns[j]), int(data.index[i]))
    #             pygame.draw.rect(Win, BLACK, (int(data.columns[j]), int(data.index[i]), 5, 5))
    #         elif j == 3 :
    #             print('green')
    #             print(int(data.columns[j]), int(data.index[i]))
    #             pygame.draw.rect(Win, GREEN, (int(data.columns[j]), int(data.index[i]), 5, 5))
    #
    #         elif j == 4:
    #             print('red')
    #             print(int(data.columns[j]), int(data.index[i]))
    #             pygame.draw.rect(Win, RED, (int(data.columns[j]), int(data.index[i]), 5, 5))
    #
    #         else :
    #             # print('white')
    #             # print(int(data.columns[j]), int(data.index[i]))
    #             pygame.draw.rect(Win, WHITE, (int(data.columns[j]), int(data.index[i]), 5, 5))


 
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
