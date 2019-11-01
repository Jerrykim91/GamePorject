# import
import pygame 
import time

# 변수 
Screen_Width  = 1000  # 창 너비
Screen_Height = 700   # 창 높이

# 사용전 게임 초기화 
pygame.init()

# 게임창을 연다. ->  게임 창의 너비와 높이를 담은 튜플을 전달 
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# 대기시간
time.sleep(5)
