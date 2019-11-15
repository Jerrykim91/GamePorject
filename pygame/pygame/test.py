
import pygame, sys
import random
import numpy as np
import pandas as pd
from pygame.locals import QUIT, KEYDOWN
from RBG import *
from hwLib import *


#<기본 내용>
# 1. 초기화 및 변수 생성
# 2. 맵 데이터 로드
# 2.1 게임 관련 데이터 초기화
# 3. 윈도우 생성(사용자 환경 생성 )
# 3.1 백그라운드 드로잉
# 4. AGV 생성
#   - agv 추가
#   - 차량 이동 경로
#   -
# 5. 메인 루프생성
#   - 배경그리기
#   -전제 서피스 갱신
#   - 시스템 딜레이

# x. 게임 종료


class AGV:
    # AGV가 기본적으로 가져야할것은 무엇이 있는가 ?
    # 0. 이름
    # 1. 색상
    # 2. 좌표값 (위치값)
    # 3. 속도

    # 멤버 변수 설정
    color = GRAY
    name = None
    direction = None
    X = 0
    Y = 0

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.X = x
        self.Y = y

    # 무슨 메소드가 필요할까?
    # 1. 자기자신을 그린다.
    # 2. 방향
    # 3. 속도
    # 4. 상황판단? 이동 경로 ?
    def SetDirection(self, dir):
        self.direction = dir

    def SetSpeed(self,spd):
        self.speed = spd

    # 상황 판단 함수 생성
    def movePath(self):pass

    def thinkPath(self):pass


class  GameSite:
    # GameSite가 기본적으로 가져야할것은 무엇이 있는가 ?
    # 0. 자기자신을 그린다.
    # 1. 초기화 // 게임 종료
    # 2. 맵그리기
    # 3. 게임 초기 값
    # 멤버변수

    gMapData = None  # 맴 데이터

    def __init__(self, path = './data/Load1116.csv'):
        self.game_init()
        self.game_Map(path)
        self.game_initData()


    # 게임초기화
    def game_init(self):
        log(' Step 1_ 게임 초기화 OK ')
        pygame.init()

    # 게임종료
    def game_free(self):
        log(' Step 9_ 게임 초기화 OK ')
        pygame.quit()
        exit()

    # 맵 로드
    # 예외처리
    def game_Map(self, path):
        try:
            self.gMapData = pd.read_csv('./data/site3.0.csv')
        except Exception as e:
            log(" 맵 데이터를 불러오지 못함!!_ 재확인 필요!! ",e)
            self.game_free()
        else:
            log('step2 맵 데이터 로드 OK')
        finally:
            pass

    #게임 관련 데이터 초기화
    def game_initData(self):
        self.WIDTH  = WIDTH
        self.HEIGHT = HEIGHT
        self.MARGIN = MARGIN
        self.WINDOW_W, self.WINDOW_H = (WINDOW_SIZE_W, WINDOW_SIZE_H)
        # 배경 이미지 생성
        self.backgroundImg = pygame.image.load(RES_PATH + BG_IMG)
        # 사용자 ui 생성
        self.screen = pygame.display.set_mode((self.WINDOW_W, self.WINDOW_H))
        # 드로잉이 로드가 걸림
        self.CLOCK = pygame.time.Clock()
        #  캡션 설정
        pygame.display.set_caption(WINDOW_CAPTION)
        # 구동 플러그
        self.Run = True

    # 겸자
    def background(self, bg, screen):
        screen.blit(bg,(0,0))
        # 박스 이동을 보기 위한 칸처리
        for row in range(60):
            # 수평선
            pygame.draw.line(screen, (64, 64, 64), (row * 10, 0), (row * 10, 500))
            for row in range(50):
                # 수직선
                pygame.draw.line(screen, (64, 64, 64), (0, row * 10), (600, row * 10))

    # 루프 생성
    def game_run(self):
        while self.Run:
            Events = pygame.event.get()
            for event in Events:
                if event.type == QUIT:
                    self.Run = False

            # 배경그리기
            self.background(self.backgroundImg, self.screen)

            # 전체 서피스 갱신
            pygame.display.flip()
            # self.CLOCK.tick(500)
            pygame.time.delay(100)

if __name__ == '__main__':
    # 차량을 어떻게 그릴 것인가 ?

    ai = GameSite()
    if ai:

        ai.game_run()
        ai.game_free()

        pass
