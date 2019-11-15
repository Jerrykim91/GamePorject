# import
import pygame
import random  # 사과의 임의 위치를 위해서 필요
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pygame.locals import QUIT, KEYDOWN
from RBG import *

#===============================
# unload : 0  , load = 1 ,
#
# = 2 ,  = 3
#
# __home point = 9__
# home_ in : 4  , home_out : 5
#
# __M = 8__
# M_in : 6  , M _out : 7
#===============================

# 변수
DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN : 'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}

BLOCK_SIZE = 20
Window_Size = [500, 600]

def draw_background(screen):
    """게임의 배경을 그린다."""
    background = pygame.Rect((0, 0), (Window_Size[0], Window_Size[1]))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position): # 좌표 값을 말하는 건가 position
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

# random.randint(1, 10)  # Integer from 1 to 10, endpoints included
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
    WIDTH = 10  # 판의 너비
    HEIGHT = 10  # 판의 높이

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
