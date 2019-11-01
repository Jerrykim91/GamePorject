<<<<<<< HEAD
# import
import pygame 
import time

# 사용전 게임 초기화
pygame.init()

# 변수 
SCREEN_WIDTH  = 400  # 창 너비
SCREEN_HEIGHT = 400  # 창 높이
BLOCK_SIZE    = 20   # 블록 고정

# 여러가지 색
# 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255


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

# 전체 화면에서 흰 사각형을 그린다. 
rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.draw.rect(screen, WHITE, rect)

# 전체 화면에서 빨간 사각형을 그린다. 
rect = pygame.Rect((340, 60), (60, 20))
pygame.draw.rect(screen, RED, rect)

# 전체 화면에서 녹색 사각형을 그린다. 
rect = pygame.Rect((0, 0), (40, 40))
pygame.draw.rect(screen, GREEN, rect)

block_position = [0, 0]  # 블록의 위치 (y, x)
Run = True

while Run:
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # 입력된 키가 위쪽 화살표 키인 경우
                block_position[0] -= 1  # 블록의 y 좌표를 1 뺀다
            elif event.key == pygame.K_DOWN:  # 입력된 키가 아래쪽 화살표 키인 경우
                block_position[0] += 1  # 블록의 y 좌표를 1 더한다
            elif event.key == pygame.K_LEFT:  # 입력된 키가 왼쪽 화살표 키인 경우
                block_position[1] -= 1  # 블록의 x 좌표를 1 뺀다
            elif event.key == pygame.K_RIGHT:  # 입력된 키가 왼쪽 화살표 키인 경우
                block_position[1] += 1

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, GREEN, block_position)
    pygame.display.update()
=======
# import
import pygame 
import time
import sys

# 변수 
Screen_Width  = 800  # 창 너비
Screen_Height = 700  # 창 높이
BLOCK_SIZE    = 10   # 블록 고정 

# 여러가지 색
# 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255

# 사용전 게임 초기화 
pygame.init()

# 게임창을 연다. ->  게임 창의 너비와 높이를 담은 튜플을 전달 
# 1000*700 픽셀을 가진 Screen
SCREEN = pygame.display.set_mode((Screen_Width, Screen_Height))

# 블록 그리는 함수 정의 하기
def Draw_Background(SCREEN):
    """ 게임의 배경을 그린다. """
    background  = pygame.Rect((0, 0), (Screen_Width, Screen_Height))
    pygame.draw.rect( SCREEN, WHITE, background )

def Draw_Block(SCREEN, color, position):
    """ position 위치에 color 블록을 그린다. """
    block  = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
   
    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect(SCREEN, color, block)


# 전체 화면에서 흰 사각형을 그린다. 
RECT = pygame.Rect((0, 0), (Screen_Width, Screen_Height))
pygame.draw.rect(SCREEN, WHITE, RECT)

# 전체 화면에서 빨간 사각형을 그린다. 
RECT = pygame.Rect((340, 60), (60, 20))
pygame.draw.rect(SCREEN, RED, RECT)

# 전체 화면에서 녹색 사각형을 그린다. 
RECT = pygame.Rect((0, 0), (40, 40))
pygame.draw.rect(SCREEN, GREEN, RECT)

# 대기시간
# time.sleep(5)

# Is_Running = True

# while True:
#     events  = pygame.event.get()   
#                                           # 발생한 이벤트를 읽어 드린다. => 리스트에 담아서 ~ 
#     for event in events:                  # 이벤트 목록을 순회하여 각 이벤트를 처리한다. 
#         if event.type == pygame.QUIT: 
#             # pygame.quit()               # 종료 이벤트가 발생한 경우 
#             exit()                        # 게임을 종료한다.  
#         if event.type == pygame.KEYDOWN:  # 이벤트 종류가 키 입력 이벤트이면
#            block_position[1] += 1         # 블록을 오른쪽으로 한 칸 움직인다.


# #  화면을 계속 새로 그린다
# Draw_Background(SCREEN)
# Draw_Block(SCREEN, GREEN, block_position)
# pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:       # 입력된 키가 위쪽 화살표 키인 경우
                block_position[0] -= 1         # 블록의 y 좌표를 1 뺀다
            elif event.key == pygame.K_DOWN:   # 입력된 키가 아래쪽 화살표 키인 경우
                block_position[0] += 1         # 블록의 y 좌표를 1 더한다
            elif event.key == pygame.K_LEFT:   # 입력된 키가 왼쪽 화살표 키인 경우
                block_position[1] -= 1         # 블록의 x 좌표를 1 뺀다
            elif event.key == pygame.K_RIGHT:  # 입력된 키가 왼쪽 화살표 키인 경우
                block_position[1] += 1         # 블록의 x 좌표를 1 더한다
>>>>>>> 56f247658b9771d4d336b62142fb5d57633ad0d5
