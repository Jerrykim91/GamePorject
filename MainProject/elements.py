# import
import pygame
import random  # 사과의 임의 위치를 위해서 필요
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pygame.locals import QUIT, KEYDOWN
from RBG import *


DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN : 'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}


# random.randint(1, 10)  # Integer from 1 to 10, endpoints included
class Agv:
    """ Agv 클래스 """
    color = GRAY  # Agv의 색

    def __init__(self):
        self.positions = [(1, 1)]  #  Agv 위치
       # self.direction = 'north'  # Agv 의 방향  => 시계방향

    def draw(self, screen):
        """  Agv 화면에 그린다. """
        for position in self.positions:  # 여러개의 블록으로 이루워져있어 for문으로 순회하며 그리도록함
            draw_block(screen, self.color, position)

    # def crawl(self):
    #     """ 현재 방향으로 한 칸 기어간다."""
    #     head_position = self.positions[0]
    #     y, x = head_position
    #     if self.direction == 'north':
    #         self.positions = [(y - 1, x)] + self.positions[:-1]
    #     elif self.direction == 'south':
    #         self.positions = [(y + 1, x)] + self.positions[:-1]
    #     elif self.direction == 'west':
    #         self.positions = [(y, x - 1)] + self.positions[:-1]
    #     elif self.direction == 'east':
    #         self.positions = [(y, x + 1)] + self.positions[:-1]
    #
    # def turn(self, direction):
    #     """ Agv 방향을 바꾼다 """
    #     self.direction = direction

    # 게임 오버 판정
    #is_game_over = agv 가 충돌하면 에러


# class Machine (object):
#     """ Machine 클래스 """
#
#     pass
#
# class Worker(object):
#     """ Worker 클래스 """
#     pass

# class Load (object):
#     """ Load 클래스 """
#     pass

class Reward(object):
    """ Reward 클래스 """
    color = RED  # 사과(보상) 색

    def __init__(self, position=(5, 5)):
        self.position = position  # 위치 => 정해진 곳에 랜덤으로 나와야함

    def draw(self, screen):
        """사과를 화면에 그린다."""
        draw_block(screen, self.color, self.position)

class Site(object):
    """ Site 클래스"""
    WIDTH = 10  # 게임판의 너비
    HEIGHT = 10  # 게임판의 높이

    def __init__(self):
        self.agv = Agv()  # 게임판 위의 Agv
        self.reward = Reward()  # 게임판 위의 사과

    def draw(self, screen):
        """ 화면에 게임판의 구성요소를 그린다."""
        self.reward.draw(screen)  # 게임판 위에 사과를 그린다.
        self.agv.draw(screen)  # 게임판 위에 agv을 그린다.

    # def process_turn(self):
    #     """게임을 한 차례 진행한다."""
    #     self.agv.crawl()  # 뱀이 한 칸 기어간다.
    #     # 게임 진행 프로세스를 수정해 0.3초가 지날 때마다 process_turn() 메서드를 호출
    #     # 뱀의 머리가 뱀의 몸과 부딛혔으면
    #     # if self.snake.positions[0] in self.snake.positions[1:]:
    #     #     raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다
    #     if self.agv.positions[0] == self.reward.position:
    #         self.put_new_apple()  # 사과를 새로 놓는다

    # def put_new_apple(self):
    #     """게임판에 새 사과를 놓는다"""
    #     # 사과를 y,x 축 0-19 사이 임의의 위치에 놓음 => 정해진 자리 좌표 입력
    #     self.reward = Reward((random.randint(0, 19), random.randint(0, 19)))
    #
    #     for position in self.agv.positions:  # agv 블록을 순회하면서
    #         if self.reward.position == position:  # 사과가 뱀위치에 놓인 경우를 확인해
    #             self.put_new_apple()  # 사과를 새로 놓는다
    #             break
