#import
import pygame 
import time

# 변수 
Screen_Width  = 1000  # 창 너비
Screen_Height = 700   # 창 높이

# 사용전 게임 초기화 
# pygame.init() 

# 게임창을 연다. ->  게임 창의 너비와 높이를 담은 튜플을 전달 
# 1000*700 픽셀을 가진 Screen
Screen = pygame.display.set_mode(( Screen_Width, Screen_Height ))

# 대기시간
time.sleep(5)


#####

# 전체 화면에서 사각형을 그린다. 

rect = pygame.Rect()
