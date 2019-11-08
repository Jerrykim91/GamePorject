import pygame , sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
 
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 5
HEIGHT = 5
MARGIN = 1
x = 0
y = 0
#-----
WINDOW_SIZE = [600, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed")
clock = pygame.time.Clock()
#-----
# grid = []
# for row in range(600):
#     #각 셀을 보유 할 빈 배열을 추가하십시오.
#     grid.append([])
#     for column in range(500):
#         grid[row].append(0)  
 
# # grid[1][5] = 1
pygame.init()

data = pd.read_csv( "./data/site1.csv", sep="," )

screen.fill(WHITE)
done = False
# -------- 메인 프로그램 루프 -----------
while not done:
    for event in pygame.event.get():  
        if event.type == QUIT: 
            done = True  

    for row in data:
        for column in data:
            Each = row,column 
            x = x + 1
            y = y + 1
            if Each == "1":
                # Color = BLACK
                pygame.draw.rect(Win, BLACK, (x, y, WIDTH, HEIGHT))

            elif x == "3":
                # Color = GREEN
                pygame.draw.rect(Win, GREEN, (x, y, WIDTH, HEIGHT))

            elif x == "4":
                # Color = PURPLE
                pygame.draw.rect(Win, PURPLE, (x, y, WIDTH, HEIGHT))

            else: 
                Color = WHITE
                pygame.draw.rect(Win, WHITE, (x, y, WIDTH, HEIGHT))


    # # Draw the 그리드
    # for row in range(600):
    #     for column in range(500):
    #         color = WHITE
    #         if grid[row][column] == 1:
    #             color = GREEN
    #         pygame.draw.rect(screen,
    #                          color,
    #                          [(MARGIN + WIDTH) * column + MARGIN,
    #                           (MARGIN + HEIGHT) * row + MARGIN,
    #                           WIDTH,
    #                           HEIGHT])
 
    clock.tick(60)
 
    pygame.display.flip()
 
pygame.quit()

"""
1. 창생성
    - 600 * 500
    - 데이터 셋 만들기 
        - 
2. 이벤트 생성 
 - 

"""