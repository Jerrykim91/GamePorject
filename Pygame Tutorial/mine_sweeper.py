#  게임으로 배우는 파이썬 교재를 기반으로 실습
""" mine_sweeper.py"""

# import
import sys
import pygame
from math import floor
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from RBG import *

# 변수
# EMPTY(빈타일) , BOMB(폭탄), OPENED(열린타일)
WIDTH = 20  # 가로방향
HEIGHT = 15 # 세로방향
SIZE = 50   # 1칸의 가로세로 크기
NUM_OF_BOMBS = 20 # 폭탄수
EMPTY = 0   # 빈타일
BOMB = 1    # 폭탄
OPENED = 2  # 열린타일
OPEN_COUNT = 0 # 열린 타일 수
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] # 타일의 상태를 이미 확인 했는지 기록하는 배열

# 초기화
pygame.init()
# 창 설정
SCREEN = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock() # CPU를 성능을 조절하기 위해서는 필수

pygame.display.set_caption("지뢰찾기")

# 폭탄수를 반환하는 함수
def num_of_bomb(field, x_pos, y_pos):
    """ 주위에 있는 폭탄 수를 반환한다 """
    count = 0
    # 이중 루프문을 사용해 x,y 축을 동시에 변화 시킨다.
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            # xpos, ypos : 좌표값
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] == BOMB:
                count += 1
    return count

# 가장 중요한 함수**
def open_tile(field, x_pos, y_pos):
    """ 타일을 오픈"""
    # 열린 타일수를 가진 OPEN_COUNT 변수
    global OPEN_COUNT
    # 타일의 검사여부를 확인하기위해 필요
    if CHECKED[y_pos][x_pos]: # 이미 확인 된 파일
        return

    CHECKED[y_pos][x_pos] = True
# 이중루프를 사용하여  x,y 축 -1,0,1 로 변화시키고 주위 좌표를 취득
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and \
                    not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)
# 메인 함수
def main():
    """ 메인 루틴 """
    # 폰트 , 메세지, 직사각형을 초기화
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!", True ,(0,255,255))
    message_over = largefont.render("!!GAME OVER!!", True, (0, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    game_over = False

# 리스트 내포 표기를 이중으로 해서 2차원 배열을 초기화
    field = [[EMPTY for xpos in range(WIDTH)]for ypos in range(HEIGHT)]

    # 폭탄 설치_ 같은곳에 폭탄이 배치하지 않도록 검사
    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH-1),randint(0, HEIGHT-1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1
# 메인루프에 진입
    run = True
    while run:
        is_space_down = False

        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 :
                xpos, ypos = floor(event.pos[0] / SIZE), \
                             floor(event.pos[1] / SIZE)
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field , xpos, ypos)

        # 그리기
        SCREEN.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SCREEN,(192, 192, 192), rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SCREEN,(255,255,0),rect)

                elif tile == OPENED:
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        num_image = smallfont.render(
                            "{}".format(count), True, (255, 255, 0))
                        SCREEN.blit(num_image,
                                     (xpos * SIZE + 10, ypos * SIZE + 10))

        # 선 그리기
        for index in range(0, WIDTH*SIZE, SIZE):
            pygame.draw.line(SCREEN, (96, 96, 96), (index, 0), (index, HEIGHT*SIZE))
        for index in range(0, HEIGHT*SIZE, SIZE):
            pygame.draw.line(SCREEN, (96, 96, 96), (0, index), (WIDTH*SIZE, index))

        # 메세지 나타내기
        if OPEN_COUNT == WIDTH*HEIGHT - NUM_OF_BOMBS:
            SCREEN.blit(message_clear, message_rect.topleft)
        elif game_over:
            SCREEN.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()