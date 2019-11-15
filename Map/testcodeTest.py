import pygame, sys
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
path = './data/img_B0.png'
#-----
WINDOW_SIZE = [600, 500]
Win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed")
clock = pygame.time.Clock()
backgroundImg = pygame.image.load(path)
#-----

data = pd.read_csv('./data/Load1116.csv')




for i in range(data.shape[0]): # 500 = i = row
    for j in range(data.shape[1]): # 600
        if data.iloc[i, j] == 1:
            Color = HEXGRAY
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 2:
            Color = BBARRY
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 3:
            Color = RED
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 4:
            Color = BLUE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 5:
            Color = YELLOW
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        elif data.iloc[i, j] == 6:
            Color = YELLOW
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        # elif data.iloc[i, j] == 7:
        #     Color = BLUE
        #     pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        # elif data.iloc[i, j] == 8:
        #     Color = YELLOW
        #     pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))
        else:
            Color = WHITE
            pygame.draw.rect(Win, Color, (int(data.columns[j]), int(data.index[i]), 1, 1))

for row in range(60):
    # 수평선
    pygame.draw.line(Win, (64, 64, 64), (row * 10, 0), (row * 10, 500))
    for row in range(50):
        # 수직선
        pygame.draw.line(Win, (64, 64, 64), (0, row * 10), (600, row * 10))
# def background(self, bg, Win):
#     Win.blit(bg,(0,0))
#     # 박스 이동을 보기 위한 칸처리

done = False
# -------- 메인 프로그램 루프 -----------
while not done:

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    clock.tick(60)
    pygame.display.update()

    #pygame.image.save(Win,'./data/new1116.png')
pygame.quit()
