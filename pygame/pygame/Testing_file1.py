# import
import pygame, sys
import random
from random import randint
import numpy as np
import pandas as pd
from pygame.locals import QUIT,KEYDOWN,Rect
from RBG import *
from hwLib import *


# Agv 클래스
class Agv:
    # 멤버변수
    color = GRAY  # Agv의 색
    _x = 0 # 좌표
    _y = 0
    # 이미지 효과
    cnt = 0

    # 생성자
    def __init__(self,color,name,x,y):
        self.color = color
        self.name = name
        self._x = x
        self._y = y


    # Agv 화면에 그린다.
    def AGVdraw(self, screen):
        self.cnt += 1
        if self.cnt % 2:
            # 판단
            self.checkAVGPath()
            # 그리기
            model = pygame.Rect((self._x * WIDTH + MARGIN, self._y * HEIGHT + MARGIN), (WIDTH, HEIGHT))
            pygame.draw.rect(screen, self.color, model)


    # agv 방향
    def SetDir(self, dir):
        self.dir = dir

    # 이동 경로
    def checkAVGPath(self):
        # position = self.positions[0]
        #  _y, _x = position
        # if self.dir == DIR_N:
        #     self.positions = [(_y - 1, _x)] + self.positions[:-1]
        #     pass
        # elif self.dir == DIR_S:
        #     self.positions = [(_y + 1, _x)] + self.positions[:-1]
        #     pass
        # elif self.dir == DIR_W:
        #     self.positions = [(_y, _x - 1)] + self.positions[:-1]
        #     pass
        # else:
        #     self.positions = [(_y, _x + 1)] + self.positions[:-1]
        #     self._x += self.speed
        #     pass

        # 상하좌우 판단하여 1칸씩 이동
        # 맵의 정보 -> 4방향에 대해서 체크해서
        # 1. 4방향 타일 체크 -> self._x, self._y => 타일의 인덱스 정보
        # self._x+1, self._x-1, self._y-1. self._y+1
        # 2. 어느방향으로 갈것인지 결정
        # 3. 이동(속도세팅은 되어 있고)

    # # 게임 오버 판정
    # def is_game_over(slef) :pass
    #     #agv 가 충돌하면 에러



# 맵 클래스 생성
class GameMap:
    # 맴버변수
    gMapData = None # 맵 데이터
    # 로봇
    robots = []

    def __init__(self,path='./data/site3.0.csv'):
        self.reward = Reward()
        #self.agv = Agv(color,name,x,y)
        self.game_init_Data()
        self.game_loadMap(path)
        self.game_init()
        # self.map_data()

    # step1 게임 초기화
    def game_init(self):
        log('step1 게임 초기화 OK')
        pygame.init()

    # step9 게임 종료
    def game_free(self):
        log('step9 게임 종료 OK')
        pygame.quit()
        import sys
        sys.exit()

    # step2 맵 데이터 로드
    def game_loadMap(self, path):
        try:
            self.gMapData = pd.read_csv('./data/site3.0.csv')
        except Exception as e:
            log('맵 데이터를 불러오지 못했습니다. 종료합니다.', e)
            self.game_free()
        else:
            log('step2 맵 데이터 로드 OK')
        finally:
            pass

    def game_init_Data(self):
        # 수치값 및 이미지 경로는 향후 전부 바깥으로 뺀다
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MARGIN = MARGIN
        self.WINDOW_W, self.WINDOW_H = (WINDOW_SIZE_W, WINDOW_SIZE_H)
        # 배경 이미지 생성
        self.backgroundImg = pygame.image.load(RES_PATH + BG_IMG)
        # 윈도우 생성
        self.screen = pygame.display.set_mode((self.WINDOW_W, self.WINDOW_H))
        # 드로잉이 로드가 걸리므로, 랜더링의 딜레이를 위한값 획득
        self.CLOCK = pygame.time.Clock()
        # 윈도의 제목 설정
        pygame.display.set_caption(WINDOW_CAPTION)
        # 게임 구동 플레그값
        self.Run = True

    # def process_turn(self):
    #     self.agv.checkAVGPath()  # 차량이
    #     if self.agv.positions[0] == self.reward.position:
    #         self.put_new_reward()

    # 보상 셋팅
    def put_new_reward(self):
        position = self.positions[0]
         _y, _x = position
            self.reward = Reward((random.randint(0, 19), random.randint(0, 19)))
            for position in self.agv.positions:  # 확인
                if self.reward.position == position:  # 위치를 확인
                    self.put_new_reward()  # 새로 놓는다
                    break


    # 배경 눈금 그리기
    def draw_background(self, bg, screen):
        screen.blit(bg, (0, 50))
        # 박스 이동을 보기 위한 칸 처리
        for row in range(60):
            # 수평선
            pygame.draw.line(screen, (64, 64, 64), (row * 10, 0), (row * 10, 600))
            # 수직선
            pygame.draw.line(screen, (64, 64, 64), (0, row * 10), (600, row * 10))

    # 시스템 구동
    def game_run(self):
        while self.Run:
            self.CLOCK.tick(30)
            EVENTS = pygame.event.get()
            for event in EVENTS:
                if event.type == QUIT:
                    self.Run = False

                    # 배경 그리기
                    self.draw_background(self.backgroundImg, self.screen)
                    # 전체 서피스 갱신
                    pygame.display.flip()
                    # self.CLOCK.tick(500)
                    pygame.time.delay(100)





# 보상 클래스
class Reward:pass
    #
    # def __init__(self):pass
    #
    #
    # def draw(self):pass


#
#

if __name__ == '__main__':
    works = GameMap()
    if works:
        # step2 맵 데이터 로드
        # step3 윈도우 생성및 초기화
        # step4 윈도우에 지형지물 배치
        # step5 AGV 생성 및 드로잉
        # step6 AGV에 딥러닝을 적용한 이동 시뮬레이션 처리, 로그기록(고민)
        # step7 조작 컨트롤러(일시정지, 제개, 등등..) 생략가능
        # step8 게임 종료
        # ai.game_free()
        pass