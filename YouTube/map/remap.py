import pygame
import sys
from pygame.locals import QUIT
from Setup import *

# from mcpi.minecraft import Minecraft
# Surface
Win = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Test")

# mc = Minecraft.create()

# blockType
LOAD  = 1 # 길
WALL  = 0 # 벽
HOME  = 2 # 집
 
# csv: 데이터 파일
data = "site1.csv"
 
# 데이터 파일 오픈
f = open(data, "r")
 
# 현재 플레이어의 위치값 가져오기
pos = mc.player.getTilePos()
orgX = pos.x+1
orgY = pos.y
# orgZ = pos.z+1
 
# z = orgZ
 
# 파일에서 데이터를 한 라인씩 읽어와서 처리함
for line in data.readlines():
  # 라인: 0,1,1,0,0,1 과 같은 형태로 데이터가 저장되어 있음
  blockList = line.split(",")
   
  # 라인별로 x좌표의 위치를 처음(orgX)로 이동
  x = orgX
   
  # 0은 빈 공간을 의미, 1은 블럭 한개를 의미
  for index in blockList:
      for columns in blockList:
    if index == "0":
      blockType = LOAD
    else:
      blockType = WALL
    # 2개층으로 만듦 -> 동일한 x, z좌표에 y 좌표 2곳에 블럭 생성
    blockType_R = pygame.draw.rect( win, x, orgY, blockType )
    blockType_W = pygame.draw.rect( win, x, orgY + 1, blockType )
    blockType_B = pygame.draw.rect( win, x, orgY + 1, blockType )

# (win,(R,G,B),(x, y, width, height))
    # rect = (x, y, width, height)
    # pygame.draw.rect(Win, RED, rect)
    # 바닥 블럭 생성
    mc.setBlock(x, orgY - 1, z, FLOOR)
     
    x = x + 1
  z = z + 1