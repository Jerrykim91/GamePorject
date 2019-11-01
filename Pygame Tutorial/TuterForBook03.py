#  게임으로 배우는 파이썬 교재를 기반으로 실습
""" draw_ lines2.py"""
# import
import pygame
import sys
from pygame.locals import QUIT

# 초기화
pygame.init()
# 변수
SCREEN_W, SCREEN_H = 400, 300

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
pygame.display.set_caption("바둑판 만들기")

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
    # 하얀색 : 세로줄
    for xpos in range(0, 400, 5):
        pygame.draw.line(SCREEN, BLACK, (xpos, 0), (xpos, 300))  # 해보고 확인 해보자 0xffffff
    # 하얀색 : 가로줄
        for ypos in range(0, 300, 5):
            pygame.draw.line(SCREEN, BLACK, (0, ypos), (400, ypos))  # 해보고 확인 해보자 0xffffff

    pygame.display.update()
    FPSCLOCK.tick(3)


if __name__=='__main__':
    main()

