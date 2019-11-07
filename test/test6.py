# import
import pygame
import sys
import numpy as np
from pygame.locals import QUIT
from Setting import *

# init => 초기화
pygame.init()

# 변수 @ Setting

# 윈도우 생성
Win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()

# 타이틀
pygame.display.set_caption("Test Project")

# 메인 함수 생성 -------
def main():
 """ main routine """

Run = True
# 이벤트 생성
while Run:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            # Run = False
            sys.exit() # 종료

    data = pd.read_csv( ".\site2.csv", sep=",", dtpye='unicode' )
    Win.fill(WHITE) 

    for index in data : 
        for columns in data :
            x = 0
            if x == 1:
                x1 = pygame.draw.rect(Win, BLACK, (x, y, width, height))
                print(x1)
            elif x == 2:
                x2 = pygame.draw.rect(Win, GREEN, (x, y, width, height))
                print(x2)
            elif x == 3:
                x3 = pygame.draw.rect(Win, PURPLE, (x, y, width, height))
                print(x3)
                else: 
                    x0 = pygame.draw.rect(Win, WHITE, (x, y, width, height))
                    print(x0)
        
# (win,(R,G,B),(x, y, width, height)) _  사각형 만들기 (win,(R,G,B),(x좌표, y좌표, width, height))
# pygame.draw.rect(Win, RED, (x, y, width, height),2)

"""
< 자연코드>

1. csv 파일을 불러온다  
2. csv 에서 데이터를 불러온다 
    data = pd.read_csv( ".\GameProject\PPdata\site2.csv", sep=",", dtpye='unicode' )

3. 데이터를 불러온것을 검사한다 
    - 어떻게 ?  for 문이랑 데이터랑 조합할건데 ?? 
    데이터가 리드 되는 동안 
        반복한다 data index 를 
            반복한다 data columns를 
            변수 초기화
                만약에 1이 나오면 # 
                    검정색 사각형을 출력한다  
                만약에 2이 나오면 
                    초록색 사각형을 출력한다
                만약에 3이 나오면 
                    보라색 사각형을 출력한다
                그외 :
                    흰색을 출력한다.

data = pd.read_csv( ".\GameProject\PPdata\site2.csv", sep=",", dtpye='unicode' )
Win.fill(WHITE) 

     while data :
        for index in data : 
            for columns in data :
                x = 0
                if x == 1:
                    x1 = pygame.draw.rect(Win, BLACK, (x, y, width, height))
                    print(x1)
                elif x == 2:
                    x2 = pygame.draw.rect(Win, GREEN, (x, y, width, height))
                    print(x2)
                elif x == 3:
                    x3 = pygame.draw.rect(Win, PURPLE, (x, y, width, height))
                    print(x3)
                    else: 
                        x0 = pygame.draw.rect(Win, WHITE, (x, y, width, height))
                    print(x0)

        break
4. 0,1,2,3 으로 분류 된 데이터가 있는 자리에 사각형을 그린다. 
"""

# 화면 갱신
pygame.display.update()
FPSCLOCK.tick(5)

if __name__=='__main__':
    main()
