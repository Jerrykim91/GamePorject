#  게임으로 배우는 파이썬 교재를 기반으로 실습
""" cave.py"""

# import
import pygame
import sys
import random
from pygame.locals import QUIT

# 초기화
pygame.init()
# 변수
SCREEN_W, SCREEN_H = 400, 300
# x, y = [0, 0]

# 여러가지 색
# 0-255 ( R, B, G )
RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127   # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0        # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 창 설정
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
FPSCLOCK = pygame.time.Clock() # CPU를 성능을 조절하기 위해서는 필수
# 타이틀
pygame.display.set_caption("렌덤 라인 만들기")

# 메인 함수 생성
def main():
 """ main routine """

run = True
while run:
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((255, 255, 255))  # 흰색으로 화면을 채운다.
    pointlist = []
    for _ in range(10):
        xpos = random.randint(0, 400)
        ypos = random.randint(0, 300)
        pointlist.append((xpos,ypos))

    pygame.draw.lines(SCREEN, BLACK,True,pointlist,5)
    pygame.display.update()
    FPSCLOCK.tick(3)


if __name__=='__main__':
    main()

