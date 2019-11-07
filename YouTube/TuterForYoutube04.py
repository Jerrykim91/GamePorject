# import
import pygame
import sys
from pygame.locals import QUIT
# from Setup import *
# init => 초기화 
pygame.init()

# 변수
width  = 64
height = 64 # 블록 사이즈인데 64 인이유는 사진때문에
# 좌표값_ 시작 위치 값이라고 보면 될 듯 
x = 50
y = 400
# BLOCK_SIZE    = 10   # 블록 고정 
vel = 5
Screen_Width  = 500  # 창 너비
Screen_Height = 480  # 창 높이
# 점프
isJump = False
jumpCount = 10
# 좌우 
left  = False
right = False
walkCount = 0

# 여러가지 색 // 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255

#  윈도우 생성
Win = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Test Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

def redrawGameWindow():
    global walkCount
    # 맵 그리기
    Win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0 

    if left : 
        Win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        Win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        Win.blit(char, (x,y))
    # (win,(R,G,B),(x, y, width, height))
    # rect = (x, y, width, height)
    # pygame.draw.rect(Win, RED, rect)
    pygame.display.update()# 화면 갱신

# 메인 루프 
Run = True

while Run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == QUIT:
            Run = False
            # exit()  # 종료

    keys = pygame.key.get_pressed()
# 키 입력
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left  = True
        right = False
    elif keys[pygame.K_RIGHT] and x < Screen_Width-vel-width:
        x += vel
        left  = False
        right = True    
    else:
        left  = False
        right = False
        walkCount = 0

    if not( isJump ):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left  = False
            walkCount = 0      
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()

