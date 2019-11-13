# snake_bite.py
import sys
import random
# from random import randint
import pygame
from RBG import *
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_DOWN, K_UP, Rect

# 초기화
pygame.init()

Window_Size = (600, 600)
screen = pygame.display.set_mode(Window_Size)
clock = pygame.time.Clock()

FOODS = []
SNAKE = []
( W, H ) = ( 20, 20 )

def add_food():
   """ 임의 장소에 먹이를 배치 """
while True:
    # 랜덤 좌표 pos를 폭과 높이의 범위내에서 구합니다
    pos = (random.randint(0, W-1), random.randint(0, H-1))
    # in 연산자를 사용해서 배열에 포함돼 있는지 판정하는것 핵심
    if pos in FOODS or pos in SNAKE:
        continue
    # 새 좌표에 FOODS에 추가하여 break로 While문을 빠져나가 호출한 곳으로 돌아옴
    FOODS.append(pos)
    break

def move_food(pos):
    """ 먹이를 다른장소로 이동 """
    # 인수의 좌표 번호를 구함
    i = FOODS.index(pos)
    # 구한 좌표를 FOODS[i]로 배열에서 삭제
    del FOODS[i]
    # 새장소에 추가
    add_food()

def paint(message):
    """화면전체 그리기"""
    screen.fill(BLACK)
    # 먹이와 뱀을 추가
    for food in FOODS:
        pygame.draw.ellipse(screen, GREEN, Rect(food[0]*30, food[1]*30, 30, 30))
    for body in SNAKE:
        pygame.draw.rect(screen, (0, 255, 255), Rect(body[0] * 30, body[1] * 30, 30, 30))
    # 판의 선을 그림
    for index in range(20):
        pygame.draw.line(screen, (64, 64, 64), (index * 30, 0), (index * 30, 600))
        pygame.draw.line(screen, (64, 64, 64), (0, index * 30), (600, index * 30))

    if message != None:
        screen.blit(message, (150, 300))
    pygame.display.update()

def main():
    """ 메인 루틴 """
    # 초기화
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    # 뱀은 화면 중앙의 1좌표 (int(W/2), int(H/2))에서 시작
    SNAKE.append((int(W/2), int(H/2)))
    # for문을 이용한 먹이 추가
    # 번호 이용을 안하기 때문에 '_'를 지정 (i,j)를 사용해도 무방
    # while len(FOODS) < 10:
    #     add_food()

    for _ in range(10):
        add_food()
# 메인 루프

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: # press 하면 key 값을 저장
                key = event.key
# 게임 오버가 아닐때 즉, 평상시 게임을 처리하는 과정
        if not game_over:
            if key == K_LEFT:
                head = (SNAKE[0][0] - 1, SNAKE[0][1])
            elif key == K_RIGHT:
                head = (SNAKE[0][0] + 1, SNAKE[0][1])
            elif key == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1] - 1)
            elif key == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1] + 1)
            # 충돌 판정
            # if head in SNAKE or \
            #         head[0] < 0 or head[0] >= W or \
            #         head[1] < 0 or head[1] >= H :
            #     message = myfont.render("Game Over!", True, (255, 255, 0))
            #     game_over = True
# 뱀을 움직이는 코드
            # 맨앞에 head를 삽입하고 만약 그장소에 먹이가 있으면 move_food(head)로 해당위치로 이동
            SNAKE.insert(0, head) # 지정된 장소에 요소를 삽입하는 메소드
            if head in FOODS:
                move_food(head)
            else:
                SNAKE.pop() # 맨 끝에서 요소를 꺼내는 메소드
        paint(message)
        clock.tick(5)

if __name__ == '__main__':
    main()

