"""
 게임 데이터 모델 정의하기
 1.  개체 정의 하기
    - 뱀, 사과 , 게임판
    # 클래스로 정의
        > 뱀
        > 사과
        > 게임판

"""

# import
import pygame
from datetime import datetime, timedelta
from datetime import timezone
from RBG import *
from pygame.locals import QUIT
# 사용전 게임 초기화
pygame.init()

# 변수  # 창의 크기가 바뀌어도 게임의 다른 영향은 없다.
SCREEN_WIDTH  = 600  # 창 너비
SCREEN_HEIGHT = 700  # 창 높이
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

# 방향키 입력에 따라 바꿀 블록의 방향
DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN : 'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}
"""
- 입력된 키가 무엇인지에 따라 방향을 적절히 바꾸루수 있도록 화살표 키와 그에 대응하는 방향을 사전으로 정의 
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
block_direction = 'east' # 블록의 방향
block_position = [0, 0]  #  좌표값 (y, x) 튜플이어야 함
last_moved_time = datetime.now()  # 마지막으로 움직인 때

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

    if timedelta(seconds=1) <= datetime.now() - last_moved_time: # 블록이 움직이고 1초가 지났으면
        if block_direction == 'north':     # 1 초가 지날때 마다
            block_position[0] -= 1          # 블록의 방향에 따라
        elif block_direction == 'south':   # 블록의 위치를 변경 한다.
            block_position[0] += 1
        elif block_direction == 'west':
            block_position[1] -= 1
        elif block_direction == 'east':
            block_position[1] += 1
        last_moved_time = datetime.now()  # 블록을 움직인 시각을 지금으로 *갱신*한다.

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, GREEN, block_position)
    pygame.display.update()


# 이동 방향만 키보드의 값으로 변경
# 좌우 같은경우 방향 전환을 하는데 상하 키를 입력하면 블록이 정지 한다. => 버그 수정함 !!
