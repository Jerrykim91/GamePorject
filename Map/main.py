# import
import pygame , sys
import pandas as pd
import numpy as np

RED = 255, 0, 0  # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0  # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255  # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127  # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0  # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127  # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255


#데이터 불러오기
data = pd.read_csv('./data/site1.csv')
# print(data)

WINDOW_SIZE = [630, 630]
# 윈도우 사이즈 계산법
# (칸수 x 블럭사이즈) +(여백(=칸수+1) x MARGIN)
#-----
# 2차원 배열 생성
# a = np.array(data)
# b = data.values
# print(a)
# print(b)
BLOCK_SIZE = 20
MARGIN = 5
WIDTH = 20
HEIGHT = 20
vel = 1
# block_position = [0, 0]


screen = pygame.display.set_mode(WINDOW_SIZE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Array Backed test")

# 한블럭당 5픽셀 씩 할당 할 것

# 2차원 배열 생성
grid = []
for row in range(25):
    grid.append([])
    for column in range(25):
        grid[row].append(0)

grid[1][5] = 1
# init => 초기화
pygame.init()
#
def draw_background(screen):
    """ 게임의 배경을 그린다. """
    # 화면 배경 설정
    screen.fill(BLACK)
    # Draw the grid
    for row in range(25): # 칸수
        for column in range(25):
            color = WHITE
            # if grid[row][column] == 1:
            #     color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

#
def draw_block(screen, color, position):
    """ position 위치에 color 블록을 그린다. """
    block = pygame.Rect(((position[1]) * WIDTH+ MARGIN, (position[0]) * HEIGHT+ MARGIN), (WIDTH, HEIGHT))
    # block = pygame.Rect((position[1] * WIDTH+MARGIN , position[0] * HEIGHT+MARGIN ), (WIDTH, HEIGHT))

    # 블록 크기 고정 ( BLOCK_SIZE, BLOCK_SIZE )
    pygame.draw.rect(screen, color, block)

block_position = [0,0]


Run = True
# -------- main loop --------
while Run:
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.QUIT:
            # Run = False
            exit()

        if event.type == pygame.KEYDOWN:
            pos = pygame.key.get_pressed()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            # print("Click ", pos, "Grid coordinates: ", row, column)

            # 키 입력
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