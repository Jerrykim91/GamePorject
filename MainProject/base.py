# import
import pygame 
import time

# 변수 
SCREEN_WIDTH  = 1000  # 창 너비
SCREEN_HEIGHT = 700   # 창 높이



# 여러가지 색 // 0-255 ( R, B, G )
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
# 윈도우 생성
Win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 대기시간
time.sleep(5)
