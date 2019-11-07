# test 작업

# import
import pygame
import sys
from pygame.locals import QUIT
# init => 초기화
pygame.init()

# 변수
x, y = (10, 10) # 좌표값
width, height = (10, 20) # 블록 사이즈 인가??
vel = 10
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 500  # 창 너비 ,창 높이 600 * 500
# BLOCK_SIZE    = 10  # 블록 고정 ??
isJump = False
jumpCount = 10

# 여러가지 색 // 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255

# 윈도우 생성
Win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()

# 타이틀
pygame.display.set_caption("Test Project")

# 메인 함수 생성
def main():
 """ main routine """

Run = True
# 이벤트 생성
while Run:
    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            # run = False
            sys.exit() # 종료

#  키를 통한 방향 값 설정
    keys = pygame.key.get_pressed()
# 키 입력
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH-width-vel:
        x += vel
    if not( isJump ):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT-height-vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
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

    # 캐릭터 그리기
    Win.fill((255, 255, 255))  # 잔상 없이 게임 생성
    # (win,(R,G,B),(x, y, width, height))
    pygame.draw.rect(Win, RED, (140, y, width, height),2)
    # 화면 갱신
    pygame.display.update()
    FPSCLOCK.tick(10)

if __name__=='__main__':
    main()
