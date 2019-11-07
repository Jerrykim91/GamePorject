#
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
# WIDTH = 5  # 가로방향
# HEIGHT= 5  # 세로방향
SIZE  = 5  # 1칸의 가로세로 크기
LODE  = 1 # BLACK
UNLODE = 0 # WHITE
HOME = 3   # PURPLE
FIELDS = []
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 500  # 창 너비 ,창 높이 600 * 500
# pos = (0, 0)  # 좌표값 (y, x) 튜플이어야 함 block_position

# map data file = site2.csv
Path ='./data/site2.csv'
f = open(Path,'r')
lines = csv.reader(f)

# csv_data = pd.read_csv('./data/site2.csv', delimiter=',')
# print(csv_data[0][0])

# 윈도우 생성
Win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()

def main():

    while True:
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Win.fill(WHITE)  # 흰색으로 화면을 채운다.
        # 그리기
        with open(Path,'r', newline='') as lines: #, newline=''
                # print(FIELDS)
            for line in lines:
                rect = (0, 0, SIZE, SIZE)
                if LODE == "1":
                    pygame.draw.rect(Win, BLACK, rect)
                elif HOME == "3":
                    pygame.draw.rect(Win, PURPLE, rect)
                else:
                    pygame.draw.rect(Win, WHITE, rect)

                    pygame.display.update()
                    FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()

# for line in f.readlines():
#     blank_list = line.split(",")
#     for block in blank_list:
#        if block == "0":
#            blockType = Wi
#        elif block == "3" :
#            blockType = Ye
#        else:
#            blockType = Ba