# import
import pygame
import random  # 사과의 임의 위치를 위해서 필요
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pygame.locals import QUIT, KEYDOWN
from RBG import *

# 사용전 게임 초기화
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
# block_position = [0, 0]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN : 'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}

def draw_background(screen):
    """게임의 배경을 그린다."""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

class Snake:
    """ 뱀 클래스 """
    color = GREEN  # 뱀의 색

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]  # 뱀의 위치
        self.direction = 'north'  # 뱀의 방향

    def draw(self, screen):
        """ 뱀을 화면에 그린다. """
        for position in self.positions:  # 뱀은 여러개의 블록으로 이루워져있어 for문으로 순회하며 그리도록함
            draw_block(screen, self.color, position)

    def crawl(self):
        """뱀이 현재 방향으로 한 칸 기어간다."""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self,direction):
        """뱀의 방향을 바꾼다 """
        self.direction = direction


    def grow(self):
        """뱀이 한 칸 자라나게 한다."""
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y - 1, x))
        elif self.direction == 'south':
            self.positions.append((y + 1, x))
        elif self.direction == 'west':
            self.positions.append((y, x - 1))
        elif self.direction == 'east':
            self.positions.append((y, x + 1))

class Apple:
    """ Apple 클래스 """
    color = RED  # 사과 색

    def __init__(self, position=(5, 5)):
        self.position = position  # 사과 위치

    def draw(self, screen):
        """사과를 화면에 그린다."""
        draw_block(screen, self.color, self.position)

class GameBoard:
    """ GameBoard 클래스 """
    width = 20  # 게임판의 너비
    height = 20  # 게임판의 높이

    def __init__(self):
        self.snake = Snake()  # 게임판 위의 뱀
        self.apple = Apple()  # 게임판 위의 사과

    def draw(self, screen):
        """ 화면에 게임판의 구성요소를 그린다."""
        self.apple.draw(screen)  # 게임판 위에 사과를 그린다.
        self.snake.draw(screen)  # 게임판 위에 뱀을 그린다.

    def process_turn(self):
        """게임을 한 차례 진행한다."""
        self.snake.crawl()  # 뱀이 한 칸 기어간다.
        # 게임 진행 프로세스를 수정해 0.3초가 지날 때마다 process_turn() 메서드를 호출
        # 뱀의 머리가 뱀의 몸과 부딛혔으면
        # if self.snake.positions[0] in self.snake.positions[1:]:
        #     raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다
        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()     # 뱀을 한 칸 자라게 한다
            self.put_new_apple()  # 사과를 새로 놓는다

    def put_new_apple(self):
        """게임판에 새 사과를 놓는다"""
        # 사과를 y,x 축 0-19 사이 임의의 위치에 놓음
        self.apple = Apple((random.randint(0,19), random.randint(0,19)))
        for position in self.snake.positions: # 뱀 블록을 순회하면서
            if self.apple.position == position:  # 사과가 뱀위치에 놓인 경우를 확인해
                self.put_new_apple()  # 사과를 새로 놓는다
                break

class SnakeCollisionException(Exception):
    """뱀 충돌 예외"""
    pass
