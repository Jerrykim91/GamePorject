import pygame
import sys
import csv
from pygame.locals import QUIT
from Setup import *

# from mcpi.minecraft import Minecraft
# Surface
Win = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Test")

# 2개층으로 만듦 -> 동일한 x, z좌표에 y 좌표 2곳에 블럭 생성
blockType_R = pygame.draw.rect( Win, RED, (1,1,1,1))
blockType_W = pygame.draw.rect( Win, WHITE, (1,1,1,1))

# blockType
LOAD  = 1 # 길
WALL  = 0 # 벽
HOME1  = 3 # in
HOME2  = 4 # out
 
# csv: 데이터 파일
data = "site1.csv"
 
# 데이터 파일 오픈
f = open(data, "r")
 
# 현재 플레이어의 위치값 가져오기
pos = [0,0]
 
# 파일에서 데이터를 한 라인씩 읽어와서 처리함
for line in f.readlines():
  # 라인: 0,1,1,0,0,1 과 같은 형태로 데이터가 저장되어 있음
  blockList = line.split(",")

  # 0은 빈 공간을 의미, 1은 블럭 한개를 의미
  for index in blockList:
      for columns in blockList:
        if index == "3":
          blockType_R = LOAD
        else:
          blockType_W = WALL

# (win,(R,G,B),(x, y, width, height))
    # rect = (x, y, width, height)
    # pygame.draw.rect(Win, RED, rect)
