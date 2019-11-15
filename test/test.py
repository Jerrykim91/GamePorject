# 원본임 ..... ;;;; 이거슨 지우면 안됨

# import
import pygame, sys
import random
import numpy as np
import pandas as pd
from pygame.locals import QUIT,KEYDOWN
from RBG import *

pygame.init()

#데이터 불러오기--------------------------
data = pd.read_csv('./data/site3.0.csv')
img = pygame.image.load('./data/img_B0.png')
# print(data)

# 변수 1 -------------------------------
WIDTH = 10
HEIGHT = 10
vel = 1
BLOCK_SIZE = 10
WINDOW_SIZE = [600, 600]

screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Room3")
CLOCK = pygame.time.Clock()


# ======= 변수 =======
DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN : 'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}



# ======= 함수 =======
def draw_background(screen):
    """ 게임의 배경을 그린다. """
    # 화면 배경 설정
    screen.blit(img, (0, 50))
    for row in range(60):
        pygame.draw.line(screen, (64, 64, 64), (row * 10, 0), (row * 10, 600))
        pygame.draw.line(screen, (64, 64, 64), (0, row * 10), (600, row * 10))

def draw_block(screen, color, position):
    """ position 위치에 color 블록을 그린다. """
    block = pygame.Rect((position[1] * WIDTH + vel, position[0] * HEIGHT + vel), (WIDTH, HEIGHT))
    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect(screen, color, block)

# ======= 클래스 =======
class Agv:
    """ Agv 클래스 """
    color = GRAY  # Agv의 색

    def __init__(self):
        self.positions = [(길 주소[0], 길 주소[1])]  #  Agv 위치(길위)
       # self.direction = ''  # Agv 의 방향  => 시계방향

    def draw(self, screen):
        """  Agv 화면에 그린다. """
        for position in self.positions:  # 여러개의 블록으로 이루워져있어 for문으로 순회하며 그리도록함
            draw_block(screen, self.color, position)

    # 게임 오버 판정
    #is_game_over = agv 가 충돌하면 에러


class Reward(object):
    """ Reward 클래스 """
    color = RED  # 보상 색

    def __init__(self, position=(?,?)):
        self.position = position  # 위치 => 정해진 곳에 랜덤으로 나와야함

    def draw(self, screen):
        """ 보상을 화면에 그린다."""
        draw_block(screen, self.color, self.position)

class Site(object):
    """ Site 클래스"""
    def __init__(self):
        self.agv = Agv()  # 판 위의 Agv
        self.reward = Reward()  # 판 위의 보상

    def draw(self, screen):
        """ 화면에 판의 구성요소를 그린다."""
        self.reward.draw(screen)  # 판 위에 보상을 그린다.
        self.agv.draw(screen)  # 판 위에 agv을 그린다.

    # def process_turn(self):
    #     """게임을 한 차례 진행한다."""
    #     self.agv.crawl()  # 차량이 한칸 움직인다
    #     # 게임 진행 프로세스를 수정해 0.3초가 지날 때마다 process_turn() 메서드를 호출
    #
    #     if self.agv.positions[0] == self.reward.position:
    #         self.put_new_reward()  # 보상을 새로 놓는다

    # def put_new_reward(self):
    #     """판에 새 보상을 놓는다"""
    #     # 보상을 y,x 축 0-19 사이 임의의 위치에 놓음 => 정해진 자리 좌표 입력
    #     self.reward = Reward((random.randint(0, 19), random.randint(0, 19)))
    #
    #     for position in self.agv.positions:  # agv 블록을 돌면서
    #         if self.reward.position == position:  # 보상이 차량 위치에 놓인 경우를 확인해
    #             self.put_new_reward()  # 보상을 새로 놓는다
    #             break



# 배열 생성------------------------------------
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        positions = data.iloc[i][j]
        if positions == 1:
            # 길
            # 길위에서 캐릭터가 움직여야해
            #print("")
        # elif positions == 2:
        #     #print("")
        # elif positions == 3:

        elif positions == 4:
           # home_ in
        elif positions == 5:
           # home_out
        elif positions == 6:
            # M_in
        elif positions == 7:
            # M_in
        elif positions == 8:
            # M
        elif positions == 9:
            # home
        else:
            # 벽
        # 충돌시 게임 아웃
            #print("야")

    # ===============================
    # unload : 0  , load = 1 ,
    #
    # = 2 ,  = 3
    #
    # __home point = 9__
    # home_ in : 4  , home_out : 5
    #
    # __M = 8__
    # M_in : 6  , M _out : 7
    # ===============================

# ==== 변수 2 ======
block_position = [0,0]
Run = True
# -------- main loop --------
while Run:
    CLOCK.tick(27)
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            Run = False

        if event.type == pygame.KEYDOWN:
            pos = pygame.key.get_pressed()
            column = pos[0] // (WIDTH + vel)
            row = pos[1] // (HEIGHT + vel)

            if event.key == pygame.K_LEFT : #block_position[1]
                block_position[1] -= vel
            elif event.key == pygame.K_RIGHT:
                block_position[1] += vel
            elif event.key == pygame.K_UP :
                block_position[0] -= vel #block_position[0]
            elif event.key == pygame.K_DOWN :
                block_position[0] += vel

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, RED, block_position)
    pygame.display.flip()

pygame.quit()
