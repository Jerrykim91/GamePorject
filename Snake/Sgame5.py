
"""
게임 데이터 모델 정의하기
 1.  개체 정의 하기
    - 뱀, 사과 , 게임판
    # 클래스로 정의
        > 뱀
            -  색
            - 머리와 몸통 위치
            - 이동방향
        > 사과
            - 색
            - 위치

        > 게임판
            - 가로 크기
            - 세로 크기
            - 올려둔 뱀
            - 올려둔 사과

    # 색, 크기 같은 것들은 고정 값이며  인스턴스에서 동일하게 사용할것이므로 클래스 속성으로 정의
    # 뱀의 위치와 방향 , 사과의 위치 , 게임판 위의 올라온 뱀과 사과는 변하는 값이고 인스턴스마다 다를수 있음 => 인스턴스 속성으로 정의
    # 인스턴스 속성들은 __init__() 함수에서 적당한 기본값을 정의해 두었다.

    # 뱀의 위치는 리스트로 정의
    # 뱀이 여러 블록으로 구성 될것  각각 리스트에 자신의 위치값을 넣어 표현 -> 사과를 먹으면 블록 위치를 더 추가해서 뱀의 길이를 늘릴것
"""

import pygame
from datetime import datetime, timedelta
from datetime import timezone
from pygame.locals import QUIT
from RBG import *

# 사용전 게임 초기화
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 방향키 입력에 따라 바꿀 블록의 방향
DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN : 'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}


# 블록 그리는 함수 정의 하기
def draw_background(screen):
    """ 게임의 배경을 그린다. """
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

# game_board = GameBoard() # 게임판 인스턴스 생성
block_direction = 'east' # 블록의 방향
block_position =[0,0]
Run = True

# ================= Main loop ========================
while Run:
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            #Run = False
            exit()

        if event.type == pygame.KEYDOWN:
            # 입력된 키가 화살표이면,
            if event.key in DIRECTION_ON_KEY:
                # 블록의 방향을 화살표 키에 맞게 바꾼다.
                block_direction = DIRECTION_ON_KEY[event.key]
                if block_direction == 'north':     # 1 초가 지날때 마다
                    block_position[0] -= 1          # 블록의 방향에 따라
                elif block_direction == 'south':   # 블록의 위치를 변경 한다.
                    block_position[0] += 1
                elif block_direction == 'west':
                    block_position[1] -= 1
                elif block_direction == 'east':
                    block_position[1] += 1

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, GREEN, block_position)

    pygame.display.update()


# 이동 방향만 키보드의 값으로 변경
# 좌우 같은경우 방향 전환을 하는데 상하 키를 입력하면 블록이 정지 한다. => 버그 수정함 !!
"""
- 입력된 키가 무엇인지에 따라 방향을 적절히 바꿀수 있도록 화살표 키와 그에 대응하는 방향을 사전으로 정의 
- 블록의 방향을 기억할수 있도록 변수 정의 
- 키보드에 입력 이벤트 발생시 입력키가 무엇인지 확인하고 사전의 키 검사는 in 연산자로 확인 가능 
- 방향키 일 경우 사전의 값을 블록의 방향 변수에 대입 
- 블록의 방향에 따라 적절하게 위치를 변경하도록 한다. (1초 간격)
# While 문은 3가지로 구성 
    - 이벤트 처리부분 
    - 시간에 따라 다른 게임을 처리하는 부분 
    - 게임 그래픽을 출력하는 부분 
> 그외는 게임에서 사용한 데이터 모델을 정의하고 게임의 규칙과 동작을 채워야한다. 
"""