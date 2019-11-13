# OOP
import random
import pygame
import sys
from RBG import *
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_DOWN, K_UP, Rect

# 초기화
pygame.init()
pygame.key.set_repeat(5,5)

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class Snake:
    """뱀 객체"""
    def __init__(self,pos):
        self.bodies = [pos]

    def move(self, key):
        """ 뱀을 1프레임만큼 이동"""
        xpos, ypos = self.bodies[0]
        if key == K_LEFT:
            xpos -= 1
        elif key == K_RIGHT:
            xpos += 1
        elif key == K_UP:
            ypos -= 1
        elif key == K_DOWN:
            ypos += 1
        head =(xpos,ypos)

        # 게임 오브 판정
        is_game_over = head in self.bodies or head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H

        self.bodies.insert(0,head)
        if head in FOODS:
            # 먹이를 다른 장소로 이동
            i = FOODS.index(head)
            del FOODS[i]
            add_food(self)
        else:
            self.bodies.pop()
        return is_game_over

    def draw(self):
        """뱀을 그린다."""
        for body in self.bodies:
            pygame.draw.rect(screen, (0,255,255),Rect(body[0]*30,body[1]*30,30,30))


FOODS = []
(W,H) =(20,20)

def add_food(Snake):
    """ 임의의 장소에 먹이를 배치 """
    while True :
        pos = (random.randint(0, W-1), random.randint(0, H-1))
        if pos in FOODS or pos in Snake.bodies:
            continue
        FOODS.append(pos)
        break

def paint(Snake , message):
    """화면 전체 그리기"""
    screen.fill((0,0,0))
    Snake.draw()
    for food in FOODS:
        pygame.draw.ellipse(screen, GREEN, Rect(food[0] * 30, food[1] * 30, 30, 30))
    for body in Snake:
        pygame.draw.rect(screen, (0, 255, 255), Rect(body[0] * 30, body[1] * 30, 30, 30))
    # 판의 선을 그림
    for index in range(20):
        pygame.draw.line(screen, (64, 64, 64), (index * 30, 0), (index * 30, 600))
        pygame.draw.line(screen, (64, 64, 64), (0, index * 30), (600, index * 30))

    if message != None:
        screen.blit(message, (150, 300))
    pygame.display.update()

def main():
    """메인루틴"""
# 초기화
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    # 뱀은 화면 중앙의 1좌표 (int(W/2), int(H/2))에서 시작
    snake = Snake((int(W/2), int(H/2)))
    for _ in range(10):
        add_food(snake)
# key 에러
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: # press 하면 key 값을 저장
                key = event.key
        if game_over:
            message =myfont.render("Game Over!", True, (255, 255, 0))
        else:
            game_over =Snake.move(key)

        paint(Snake, message)
        clock.tick(5)

if __name__ == '__main__':
    main()