# import
import pygame
import sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
from RBG import *
# from Setting import *

# 윈도우 생성
WINDOW_SIZE = [600, 500]  # col :600 raw :500
# MACHINE_SIZE = [120,100] # 기계 사이즈

Win = pygame.display.set_mode(WINDOW_SIZE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Array Backed test")



# 변수
WIDTH = 5
HEIGHT = 5
MARGIN = 1

LOAD = 1  # 길
WALL = 0  # 벽
HOME1 = 3  # in
HOME2 = 4  # out

#  데이터 셋
data = pd.read_csv('./data/site1.csv', sep=",")

Win.fill(WHITE)
# --------------------------------------------
# DATA.SHAPE = (500, 600) # col :600  raw :500
for i in range(data.shape[0]): # 500 = i = row
    for j in range(data.shape[1]): # 600
        if data.iloc[i, j] == LOAD:
            pygame.draw.rect(Win, BLACK, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 2:
            pygame.draw.rect(Win, BLUE, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == HOME1:
            pygame.draw.rect(Win, GREEN, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == HOME2:
            pygame.draw.rect(Win, RED, (int(data.columns[j]), int(data.index[i]), 1, 1))
        else:
            pygame.draw.rect(Win, WHITE, (int(data.columns[j]), int(data.index[i]), 1, 1))
# --------------------------------------------

# 메인 함수 생성-----------
def main():
    """ main routine """
Run = True
while Run:
    for event in pygame.event.get():
        if event.type == QUIT:
            Run = False
            sys.exit()  # 종료

    pygame.display.flip()
    CLOCK.tick(60)

if __name__ == '__main__':
    main()

# (win,(R,G,B),(x, y, width, height))
# rect = (Win, RED, (x, y, width, height),2)

# ----------------------
# (win,(R,G,B),(x, y, width, height)) _  사각형 만들기 (win,(R,G,B),(x좌표, y좌표, width, height))
# pygame.draw.rect(Win, RED, (x, y, width, height),2)
