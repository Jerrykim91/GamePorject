#  게임으로 배우는 파이썬 교재를 기반으로 실습
""" cave.py"""

# import
import sys
import pygame
from random import randint
from pygame.locals import QUIT, Rect, K_SPACE, KEYDOWN
from RBG import *
# 초기화
pygame.init()
pygame.key.set_repeat(5,5)

# 변수
SCREEN_W, SCREEN_H = 800, 600

# 변수
SCREEN_W, SCREEN_H = 800, 600
# x, y = [0, 0]

# 창 설정
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
FPSCLOCK = pygame.time.Clock() # CPU를 성능을 조절하기 위해서는 필수

pygame.display.set_caption("동굴 만들기")

# 메인 함수 생성
def main():
 """ 메인 루틴  """
walls = 80
ship_y = 250
velocity = 0
score = 0
slope = randint(1,6)
sysfont = pygame.font.SysFont(None, 36)
ship_img = pygame.image.load("ship.png")
bang_img = pygame.image.load("bang.png")
holes = []
game_over = False
for xpos in range(walls):
    holes.append(Rect(xpos * 10,100,10,400))
    game_over = False

run = True
# 루프구간
while run:
    is_space_down = False
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN :
            if event.key == K_SPACE:
                is_space_down = True

    # 내 캐릭터 이동
    if not game_over :
        score += 10
        velocity += -3 if is_space_down else 3
        ship_y += velocity

        # 동굴을 스크롤
        edge = holes[-1].copy()
        test = edge.move(0,slope)
        if test.top <= 0 or test.bottom >= 600:
            slope = randint(1,6) * (-1 if slope > 0 else 1)
            edge.inflate_ip(0,-20)
        edge.move_ip(10,slope)
        holes.append(edge)
        del holes[0]
        holes = [x.move(-10,0) for x in holes]

        # 충돌
        if holes[0].top > ship_y or \
            holes[0].bottom < ship_y + 80 :
            game_over = True

    # 그리기
    SCREEN.fill((0, 255, 0))
    for hole in holes:
        pygame.draw.rect(SCREEN,WHITE, hole)
    SCREEN.blit(ship_img, (0, ship_y))
    score_img = sysfont.render("score is {}".format(score), True, (0, 0, 225))
    SCREEN.blit(score_img,(600, 20))

    if game_over:
        SCREEN.blit(bang_img, (0, ship_y-40))

    pygame.display.update()
    FPSCLOCK.tick(5)

if __name__ == '__main__':
    main()


# 재시작 버튼 만들어야해