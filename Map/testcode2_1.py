import pygame
import sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT

pygame.init()
# colors // 0-255 ( R, B, G )
RED = 255, 0, 0  # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0  # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255  # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127  # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0  # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127  # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

WIDTH = 5
HEIGHT = 5
MARGIN = 1

WINDOW_SIZE = [600, 500]
Win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed")
clock = pygame.time.Clock()

#  데이터 셋
data = pd.read_csv('./data/site1.csv', sep=",")
# print(np.array(data))
print(data)

# 화면 배경 설정
Win.fill(WHITE)

grid = []
for row in range(np.array(data.shape[0])):
#     grid.append([])
# #     print(grid)
    for column in range(np.array(data.shape[1])):
        print(column)
        # grid[row].append(0)
        if data[row,column] == 1:
            Color = BLACK
            pygame.draw.rect(Win, Color, (column, row, HEIGHT, WIDTH))
        elif data[row,column] == 2:
            Color = RED
            pygame.draw.rect(Win, Color, (column, row, HEIGHT, WIDTH))
        # elif data[row][column] == 3:
        #     Color = BLUE
        #     pygame.draw.rect(Win, Color, (column, row, HEIGHT, WIDTH))
        else:
            Color = WHITE
            pygame.draw.rect(Win, Color, (column, row, HEIGHT, WIDTH))

# 행 1, 셀 5를 1로 설정하십시오. (행과 열 번호는 0에서 시작한다는 것을 기억하십시오.)
# grid[1][5] = 1


done = False
# -------- 메인 프로그램 루프 -----------
while not done:
    for event in pygame.event.get():  
        if event.type == QUIT: 
            done = True
    #
    # # Draw the 그리드
    # for row in range(data.shape[0]):
    #     for column in range(data.shape[1]):
    #         color = GRAY
    #         if grid[row][column] == 1:
    #             color = GREEN
    #         pygame.draw.rect(Win,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
 
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()