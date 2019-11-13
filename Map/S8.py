# import
import pygame
import pandas as pd
import random  # 사과의 임의 위치를 위해서 필요
from datetime import datetime
from datetime import timedelta
from pygame.locals import QUIT, KEYDOWN
from RBG import *

# 사용전 게임 초기화
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLOCK_SIZE = 20
# block_position = [0, 0]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


data = pd.read_csv('./data/site3.0.csv')

# positions = []
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        positions = data.iloc[i][j]


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
        self.positions = (1, 1)  # 뱀의 위치
        #self.direction = 'north'  # 뱀의 방향

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
           #self.snake.grow()     # 뱀을 한 칸 자라게 한다
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


game_board = GameBoard() # 게임판 인스턴스 생성
# TURN_INTERVAL = timedelta(seconds=0.3) # 게임 진행 간격을 3초로 정의한다.
# last_moved_time = datetime.now()  # 마지막으로 움직인 때
last_turn_time = datetime.now()
Run = True

# ================= Main loop ========================
while Run:
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            #Run = False
            exit()
        if event.type == KEYDOWN:
            if event.key in DIRECTION_ON_KEY:
                game_board.snake.turn(DIRECTION_ON_KEY[event.key])

    # 시간이 TURN_INTERVAL 만큼 지날 때 마다 게임을 한차례씩 진행한다.
    if timedelta(seconds=0.1) < datetime.now() - last_turn_time:
        game_board.process_turn()
        last_turn_time = datetime.now()

    # if TURN_INTERVAL < datetime.now() - last_moved_time:
    #     game_board.process_turn()
    #     last_moved_time -= datetime.now()
        # try:
        #     game_board.process_turn()
        # except SnakeCollisionException:
        #     exit()
        # last_turn_time = datetime.now()

    draw_background(screen)
    game_board.draw(screen)  # 화면에 게임판을 그린다
    pygame.display.update()



# ++++++Sgame8.py++++++++++
# 뱀의 몸이 움직이는 메서드 정의
# 게임판에 게임 진행 메서드 정의
# 일정 시간마다 게임을 한차례씩 진행하기

"""
 뱀이 사과를 먹고 자라는 것을 구현할 차례다. 그러려면 어떤 문제를 풀어야 하는지 정의해 보자.

1. 뱀이 사과를 먹었다는 것을 어떻게 인식할 것인가?
    - 뱀이 이동한 후에 뱀의 머리 위치와 사과의 위치가 똑같은 경우 뱀이 사과를 먹었다고 판단
    => 게임판의 게임 진행 메서드 process_turn()에서 판단
    - if 문으로  두블록의 위치가 같은지 확인, 같으면 여기서 뱀이 자나라도록하고 사과를 새로 생성
    - 뱀이 자라나게하는 메서드와 사과를 새로 놓는 메서드는 미정  => 호출은 이렇게 

2. 사과를 먹은 뒤 뱀이 길어지게 하려면 어떻게 할 것인가?
    - 뱀을 구성하는 블럭을 하나 추가하는 것으로 해결
    - 뱀의 맨 앞이나 맨뒤에 블록을 추가하면 되는데  이미 한 칸 기어간후이므로 맨뒤에 추가하면 ok
    - 뱀 클래스에 다음과 같이 grow() 메서드를 정의 

3. 사과를 먹은 뒤 새 사과를 어떻게 만들 것인가?
    - 사과를 새로 놓는 문제는 게임판에 놓은 사과를 새것으로 바꾸면 해결 가능하다 
    - 새로만들어지는 사과는 임의의 위치에 만들어져야 게임이 재미있을것 
    - 사과를 적절한곳에 놓는일은 게임판의 책임
        => 사과 클래스가 아니라 게임판 클래스에 put_new_apple() 메서드를 추가 
"""