# 유튜브 참조
# import
import pygame
# init => 초기화 
pygame.init()

# 변수
# 여러가지 색 // 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255

#  윈도우 생성
Win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Test Game")

x, y = (50, 50)
width, height = (40, 60)
vel = 5

Run = True
while Run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # run = False
            exit()  # 종료

#  키를 통한 방향 값 설정
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # 캐릭터 그리기
    # (win,(R,G,B),(x, y, width, height))
    pygame.draw.rect(Win, RED, (x, y, width, height))
    # 화면 갱신
    pygame.display.update()

pygame.quit()
