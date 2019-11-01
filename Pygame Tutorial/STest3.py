#  화면 밖으로 나가는 문제를 해결 할 것이다.(좌우만 해결)

# import
import pygame
# init => 초기화 
pygame.init()

# 변수
x, y = (10, 10) # ? 블락 포지션 값인가 ?
width, height = (20, 30) # 블록 사이즈 인가??
vel = 5
Screen_Width  = 1000  # 창 너비
Screen_Height = 700  # 창 높이
# BLOCK_SIZE    = 10   # 블록 고정
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

#  윈도우 생성
Win = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Test Game")

# 이벤트 생성
Run = True
while Run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # run = False
            exit()  # 종료

#  키를 통한 방향 값 설정
    keys = pygame.key.get_pressed()
# 키 입력
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < Screen_Width-width-vel:
        x += vel
    if not( isJump ):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < Screen_Height-height-vel:
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
    Win.fill((0,0,0)) # 잔상 없이 게임 생성
    # (win,(R,G,B),(x, y, width, height))
    pygame.draw.rect(Win, RED, (x, y, width, height))
    # 화면 갱신
    pygame.display.update()

pygame.quit()

