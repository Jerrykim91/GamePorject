# import
import pygame
import sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
# from Setting import *

# 여러가지 색 // 0-255 ( R, B, G )
RED = 255, 0, 0  # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0  # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255  # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127  # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0  # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127  # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 윈도우 생성
WINDOW_SIZE = [600, 500]  # col :600 raw :500
# MACHINE_SIZE = [120,100] # 기계 사이즈

Win = pygame.display.set_mode(WINDOW_SIZE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Array Backed test")

# init => 초기화
pygame.init()

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

"""
<map코드>
0. 창 생성
    - 600 * 500
    - 데이터 셋 만들기 
1. csv 파일을 불러온다  
2. csv 에서 데이터를 불러온다 
    data = pd.read_csv( ".\GameProject\PP\data\site2.csv", sep=",", dtpye='unicode' ),
    data = pd.read_csv( "site1.csv", sep="," )
    
//이벤트 생성// 
3. 데이터를 불러온것을 검사한다 
    - 어떻게 ?  for 문이랑 데이터랑 조합할건데 ?? 
    데이터가 리드 되는 동안 
        반복한다 data index 를 
            반복한다 data columns를 
            
                만약에 1이 나오면 # 
                    검정색 사각형을 출력한다  
                만약에 2이 나오면 
                    초록색 사각형을 출력한다
                만약에 3이 나오면 
                    보라색 사각형을 출력한다
                그외 :
                    흰색을 출력한다.
                    
                    
    # 이미지를 다 그리고 png 파일로 다운받아서 
    입히기 
"""
