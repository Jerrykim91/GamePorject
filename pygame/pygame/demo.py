# import
import pygame, sys
import random
import numpy as np
import pandas as pd
from pygame.locals import QUIT, KEYDOWN
from RBG import *
from hwLib import *


class AVGModel:
    # 맴버변수
    gMapData = None  # 맴 데이터

    # 생성자
    def __init__(self, path='./data/site3.0.csv'):
        self.game_init()
        self.game_loadMap(path)
        self.game_initGameData()

        self.game_run()

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

    # step6
    def game_run(self):
        while self.Run:
            self.CLOCK.tick(27)
            EVENTS = pygame.event.get()
            for event in EVENTS:
                if event.type == QUIT:
                    Run = False

    def game_drawAGV(self):
        pass

    # step7 AGV에 딥러닝을 적용한 이동 시뮬레이션 처리, 로그기록(고민)
    def game_aiCoreAGV(self):
        pass

    # step8 조작 컨트롤러(일시정지, 제개, 등등..) 생략가능
    def game_controllerAGV(self):
        pass


if __name__ == '__main__':
    ai = AVGModel()
    if ai:
        # step2 맵 데이터 로드
        # step3 윈도우 생성및 초기화
        # step4 윈도우에 지형지물 배치
        # step5 AGV 생성 및 드로잉
        # step6 AGV에 딥러닝을 적용한 이동 시뮬레이션 처리, 로그기록(고민)
        # step7 조작 컨트롤러(일시정지, 제개, 등등..) 생략가능
        # step8 게임 종료
        # ai.game_free()
        pass