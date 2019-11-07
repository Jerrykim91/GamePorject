import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
# 각 그리드 위치의 너비와 높이를 설정합니다
WIDTH = 5
HEIGHT = 5
 
# This sets the margin between each cell
# 이것은 각 셀 사이의 여백을 설정합니다
MARGIN = 1
 
# Create a 2 dimensional array. A two dimensional
# 2 차원 배열을 만듭니다. 2 차원
# array is simply a list of lists.
#배열은 단순히 목록의 목록입니다.
grid = []
for row in range(500):
    # Add an empty array that will hold each cell
    #각 셀을 보유 할 빈 배열을 추가하십시오.
    # in this row
    grid.append([])
    for column in range(500):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
# 행 1, 셀 5를 1로 설정하십시오. (행과 열 번호는 0에서 시작한다는 것을 기억하십시오.)
grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [500, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
# 사용자가 닫기 버튼을 클릭 할 때까지 반복합니다.
done = False
 
# Used to manage how fast the screen updates
# 화면 업데이트 속도를 관리하는 데 사용
clock = pygame.time.Clock()
 
# -------- 메인 프로그램 루프 -----------
while not done:
    for event in pygame.event.get():  # 사용자 이벤트
        if event.type == QUIT:  # 만약 사용자가 닫을 경우
            done = True  # 이 루프를 종료하도록 플래그를 지정
        elif event.type == MOUSEBUTTONDOWN:
            # 사용자가 마우스를 클릭 -> 위치를 얻음
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            # x / y 화면 좌표를 그리드 좌표로 변경
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            # 그 위치를 하나로 설정
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # 화면 배경 설정
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(500):
        for column in range(500):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    # 계속해서 우리가 그린 것으로 화면을 업데이트하십시오.
    pygame.display.flip()
 
pygame.quit()