# import
import pygame
from datetime import datetime, timedelta
from datetime import timezone
from RBG import *
from pygame.locals import QUIT
# 사용전 게임 초기화
pygame.init()

# 변수 
SCREEN_WIDTH  = 400  # 창 너비
SCREEN_HEIGHT = 400  # 창 높이
BLOCK_SIZE    = 20   # 블록 고정
vel = 1

# 1000*700 픽셀을 가진 Screen=> 게임 창의 너비와 높이를 담은 튜플을 전달
#  윈도우 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake_Game")

# 대기시간
# time.sleep(3)

# 블록 그리는 함수 정의 하기
def draw_background(screen):
    """ 게임의 배경을 그린다. """
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """ position 위치에 color 블록을 그린다. """
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect(screen, color, block)

# # 전체 화면에서 흰 사각형을 그린다.
# rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.draw.rect(screen, WHITE, rect)
#
# # 전체 화면에서 빨간 사각형을 그린다.
# rect = pygame.Rect((340, 60), (60, 20))
# pygame.draw.rect(screen, RED, rect)
#
# # 전체 화면에서 녹색 사각형을 그린다.
# rect = pygame.Rect((0, 0), (40, 40))
# pygame.draw.rect(screen, GREEN, rect)

block_position = [0, 0]  #  좌표값 (y, x) 튜플이어야 함
last_moved_time = datetime.now()  # 마지막으로 움직인 때

Run = True
# ================= Main loop ========================
while Run:
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            Run = False
            exit()

    if timedelta(seconds=1) <= datetime.now() - last_moved_time: # 블록이 움직이고 1초가 지났으면
        block_position[1] += 1   # 블록이 오른쪽으로 움직인다.
        last_moved_time = datetime.now() # 블록을 움직인 시각을 지금으로 *갱신*한다.

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, GREEN, block_position)
    pygame.display.update()
