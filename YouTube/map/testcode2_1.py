import pygame
import sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT, MOUSEBUTTONDOWN
 
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 5
HEIGHT = 5
MARGIN = 1

# grid = []
# for row in range(600):
#     #각 셀을 보유 할 빈 배열을 추가하십시오.
#     grid.append([])
#     for column in range(500):
#         grid[row].append(0)  
 
# 행 1, 셀 5를 1로 설정하십시오. (행과 열 번호는 0에서 시작한다는 것을 기억하십시오.)
# grid[1][5] = 1
 
pygame.init()
 
WINDOW_SIZE = [600, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed")
clock = pygame.time.Clock()

done = False
# -------- 메인 프로그램 루프 -----------
while not done:
    for event in pygame.event.get():  
        if event.type == QUIT: 
            done = True  
        # elif event.type == MOUSEBUTTONDOWN:
        #     # 사용자가 마우스를 클릭 -> 위치를 얻음
        #     pos = pygame.mouse.get_pos()
        #     # x / y 화면 좌표를 그리드 좌표로 변경
        #     column = pos[0] // (WIDTH + MARGIN)
        #     row = pos[1] // (HEIGHT + MARGIN)
        #     # 그 위치를 하나로 설정
        #     grid[row][column] = 1
        #     print("Click ", pos, "Grid coordinates: ", row, column)
 
    # 화면 배경 설정
    screen.fill(WHITE)
 
    # Draw the 그리드
    for row in range(600):
        for column in range(500):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    clock.tick(60)
 
    pygame.display.flip()
 
pygame.quit()