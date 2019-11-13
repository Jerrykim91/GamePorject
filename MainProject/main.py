import pygame, sys
import numpy as np
import pandas as pd
from pygame.locals import QUIT
from RBG import *


pygame.init()
Window_Size = [600, 500]
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
BLOCK_SIZE = 20
screen = pygame.display.set_mode(Window_Size)
clock = pygame.time.Clock()




# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()


    clock.tick(50)
    pygame.display.update()
pygame.quit()