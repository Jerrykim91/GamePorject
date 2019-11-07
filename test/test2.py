# import
import pygame
import sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT

# 여러가지 색 // 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255

# 윈도우 생성
WINDOW_SIZE = [600, 500]
Win = pygame.display.set_mode(WINDOW_SIZE)
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Array Backed test")

# init => 초기화
pygame.init()

# 변수
WIDTH = 5
HEIGHT = 5
MARGIN = 1

data = pd.read_csv( "site1.csv", sep="," )

def W_display(): # 화면 갱신
    pygame.display.update()
    FPSCLOCK.tick(5)

# 메인 함수 생성
def main():
 """ main routine """

Run = True
# 이벤트 생성
while Run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            sys.exit() # 종료
        #     column = pos[0] // (WIDTH + MARGIN)
        #     row = pos[1] // (HEIGHT + MARGIN)
        #     # 그 위치를 하나로 설정
        #     grid[row][column] = 1
        #     print("Click ", pos, "Grid coordinates: ", row, column)

    Win.fill((255, 255, 255))

    for row in data:
        grid.append([])
        for column in data:
            grid[row].append(0)  
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
                    # if grid[row][column] == 1:
                    #     color = GREEN
                    # pygame.draw.rect(screen,
                    #                 color,
                    #                 [(MARGIN + WIDTH) * column + MARGIN,
                    #                 (MARGIN + HEIGHT) * row + MARGIN,
                    #                 WIDTH,
                    #                 HEIGHT])

    # (win,(R,G,B),(x, y, width, height))
    # rect = (Win, RED, (x, y, width, height),2)
   
    W_display()

if __name__=='__main__':
    main()
