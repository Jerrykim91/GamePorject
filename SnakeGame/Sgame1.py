#import
import pygame 
import time

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
# pygame.init() 

# 게임창을 연다. ->  게임 창의 너비와 높이를 담은 튜플을 전달 
# 1000*700 픽셀을 가진 Screen
SCREEN = pygame.display.set_mode(( Screen_Width, Screen_Height ))

######################################################################
def draw_background(SCREEN):
    """ 게임의 배경을 그린다. """
    BACKGROUND = pygame.Rect((0,0),( Screen_Width, Screen_Height ))
    pygame.draw.rect( SCREEN , WHITE , BACKGROUND )

def draw_block(SCREEN, color, position):
    """ position 위치에 color 블록을 그린다. """
    BLOCK = pygame.Rect(( position[1]*BLOCK_SIZE, position[0]*BLOCK_SIZE ),( BLOCK_SIZE, BLOCK_SIZE ))
    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect( SCREEN , color , BLOCK )
######################################################################

# 전체 화면에서 흰 사각형을 그린다. 
RECT = pygame.Rect((0,0),( Screen_Width, Screen_Height ))
pygame.draw.rect( SCREEN , WHITE , RECT)

# 전체 화면에서 빨간 사각형을 그린다. 
RECT = pygame.Rect((340,60),(60,20))
pygame.draw.rect( SCREEN , RED , RECT)

# 전체 화면에서 녹색 사각형을 그린다. 
RECT = pygame.Rect((0,0),( 40,40 ))
pygame.draw.rect( SCREEN , GREEN , RECT)


pygame.display.update()

# 대기시간
# time.sleep(5)

# Is_Running = True


# 무한히 계속, 아무 일도 하지 않는다.
# while True : 
#     pass = > 창도 안 닫힘 
# 그래서 이벤트를 넣어야 함 
while True:
    EVENTS = pygame.event.get()   
                                       # 발생한 이벤트를 읽어 드린다. => 리스트에 담아서 ~ 
    for event in EVENTS :              # 이벤트 목록을 순회하여 각 이벤트를 처리한다. 
        if event.type == pygame.QUIT:  # 종료 이벤트가 발생한 경우 
             exit()                    # 게임을 종료한다. 