# import
import pygame
import pandas as pd
import sys
import csv
from pygame.locals import QUIT, Rect

# init => 초기화
pygame.init()

# 여러가지 색 // 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255

# 변수
WIDTH = 5  # 가로방향
HEIGHT= 5  # 세로방향
SIZE  = 5  # 1칸의 가로세로 크기
LODE  = 1 # BLACK
UNLODE = 0 # WHITE
HOME = 3   # PURPLE

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 500  # 창 너비 ,창 높이 600 * 500
Win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()

# map data file = site2.csv
data = pd.read_csv( './data/site1.csv', sep="," )
# print(data.columns)
Win.fill(WHITE)  # 흰색으로 화면을 채운다.

# DATA.SHAPE = (500, 600) # col :600  raw :500
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        print(data[row][col])

        # data = df.iloc[row, col]
        # if data == 1 :
        #     Color = BLACK
        #     pygame.draw.rect(Win, Color, (int(data.columns[col]), int(data.index[row]), 1, 1))
        # print(int(data.columns[col]))
        # col =
        # row =


def W_display(): # 화면 갱신
    pygame.display.update()
    FPSCLOCK.tick(5)

def main(): # 메인함수
    while True:
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()




if __name__ == '__main__':
    main()

