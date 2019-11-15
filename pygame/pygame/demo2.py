# import
import pygame, sys
import random
import numpy as np
import pandas as pd
from pygame.locals import QUIT, KEYDOWN
from RBG import *
from hwLib import *


class AVGModel:
    # 모델의 방향
    dir = None
    # 모델의 스피드
    speed = 0
    # 모델의 색상
    color = BLACK
    # 모델의 이름
    name = None
    # 모델의 좌표
    _x = 0
    _y = 0
    # 애니메이션
    cnt = 0

    def __init__(self, color, name, x, y, speed):
        self.color = color
        self.name = name
        self._x = x
        self._y = y
        self.speed = speed
        # 임시 설정
        self.setDir(DIR_E)

    def setDir(self, dir):
        self.dir = dir

    def setSpeed(self, speed):
        self.speed = speed

    def drawAVG(self, screen):
        self.cnt += 1
        if self.cnt % 2:
            # 판단
            self.checkAVGPath()
            # 그리기
            model = pygame.Rect((self._x * WIDTH + MARGIN, self._y * HEIGHT + MARGIN), (WIDTH, HEIGHT))
            pygame.draw.rect(screen, self.color, model)

    def checkAVGPath(self):
        # 상하좌우 판단하여 1칸씩 이동
        # 맵의 정보 -> 4방향에 대해서 체크해서
        # 1. 4방향 타일 체크 -> self._x, self._y => 타일의 인덱스 정보
        # self._x+1, self._x-1, self._y-1. self._y+1
        # 2. 어느방향으로 갈것인지 결정
        # 3. 이동(속도세팅은 되어 있고)
        if self.dir == DIR_N:
            # y값 감수
            pass
        elif self.dir == DIR_S:
            # y값 증가
            pass
        elif self.dir == DIR_W:
            # x값 감소
            pass
        else:  # self.dir == DIR_E:
            #  x값 증가
            self._x += self.speed
            pass


class GameBase:
    # 맴버변수
    gMapData = None  # 맴 데이터
    # 로봇들
    robots = []

    # 생성자
    def __init__(self, path='./data/site3.0.csv'):
        self.game_init()
        self.game_loadMap(path)
        self.game_initGameData()

        # self.game_run()

    # step1 게임 초기화
    def game_init(self):
        log('step1 게임 초기화 OK')
        pygame.init()

    # step9 게임 종료
    def game_free(self):
        log('step9 게임 종료 OK')
        pygame.quit()
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

    # step2-1 게임 관련 데이터 초기화
    def game_initGameData(self):
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

    # step3 윈도우 생성및 초기화
    def game_initWindow(self):
        pass

    # step4 윈도우에 지형지물 배치
    def game_drawWindow(self):
        pass

    # step5 AGV 생성 및 드로잉
    def game_initAGV(self):
        pass

    def draw_background(self, bg, screen):
        screen.blit(bg, (0, 50))
        # 박스 이동을 보기 위한 칸 처리
        for row in range(60):
            # 수평선
            pygame.draw.line(screen, (64, 64, 64), (row * 10, 0), (row * 10, 600))
            # 수직선
            pygame.draw.line(screen, (64, 64, 64), (0, row * 10), (600, row * 10))

    # step6
    def game_run(self):
        while self.Run:
            EVENTS = pygame.event.get()
            for event in EVENTS:
                if event.type == QUIT:
                    self.Run = False

            # 배경 그리기
            self.draw_background(self.backgroundImg, self.screen)
            
            # 로봇 그리기
            for avg in self.robots:
                avg.drawAVG(self.screen)
            # 전체 서피스 갱신
            pygame.display.flip()
            # self.CLOCK.tick(500)
            pygame.time.delay(100)

    def game_drawAGV(self):
        pass

    # step7 AGV에 딥러닝을 적용한 이동 시뮬레이션 처리, 로그기록(고민)
    def game_aiCoreAGV(self):
        pass

    # step8 조작 컨트롤러(일시정지, 제개, 등등..) 생략가능
    def game_controllerAGV(self):
        pass

    # 로봇 추가
    def game_addRobot(self, avgs):
        self.robots.extend(avgs)


if __name__ == '__main__':
    ai = GameBase()
    if ai:
        avg = AVGModel(RED, '1차로봇', 1, 51, 1)
        avg2 = AVGModel(GREEN, '2차로봇', 10, 10, 2)
        ai.game_addRobot([avg, avg2])
        ai.game_run()
        # step2 맵 데이터 로드
        # step3 윈도우 생성및 초기화
        # step4 윈도우에 지형지물 배치
        # step5 AGV 생성 및 드로잉
        # step6 AGV에 딥러닝을 적용한 이동 시뮬레이션 처리, 로그기록(고민)
        # step7 조작 컨트롤러(일시정지, 제개, 등등..) 생략가능
        # step8 게임 종료
        ai.game_free()
        pass