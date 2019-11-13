from RBG import *

"""
 게임 데이터 모델 정의하기
 1.  개체 정의 하기
    - 뱀, 사과 , 게임판
    # 클래스로 정의
        > 뱀
            -  색
            - 머리와 몸통 위치 
            - 이동방향 
        > 사과
            - 색 
            - 위치 

        > 게임판
            - 가로 크기 
            - 세로 크기 
            - 올려둔 뱀 
            - 올려둔 사과 

    # 색, 크기 같은 것들은 고정 값이며  인스턴스에서 동일하게 사용할것이므로 클래스 속성으로 정의 
    # 뱀의 위치와 방향 , 사과의 위치 , 게임판 위의 올라온 뱀과 사과는 변하는 값이고 인스턴스마다 다를수 있음 => 인스턴스 속성으로 정의 
    # 인스턴스 속성들은 __init__() 함수에서 적당한 기본값을 정의해 두었다. 

    # 뱀의 위치는 리스트로 정의 
    # 뱀이 여러 블록으로 구성 될것  각각 리스트에 자신의 위치값을 넣어 표현 -> 사과를 먹으면 블록 위치를 더 추가해서 뱀의 길이를 늘릴것 

 2. 개체의 동작 정의하기 
클래스에 동작(메서드)을 정의   

# 클래스로 동작 정의 
        > 뱀
            -  자기자신 그리기
            -  현재방향으로 움직이기
            -  방향 바꾸기  
            - 자라나기 
        > 사과
            - 자기 자신 그리기 
            - 

        > 게임판
            - 자기 자신 그리기
            - 자기위에 뱀과 사과 놓기 (__init__()함수에 정의한 동작)
            - 사과가 없어 지면 새로 놓기 
            - 게임을 한 차례 진행하기 
# draw 메소드는 화면에 객체를 전달받아  draw_block를 이용해  화면에 블록을 그린다. 
# 사과는 블록 한 개 뿐이어서 블록을 하나만 그림
# 게임판은 자기 위에 올라와 있는 사과와 뱀을 그리는 역할
# 게임판의 draw() 메서드를 한 번 호출할 때마다 게임 화면의 모든 구성요소를 그릴 수 있다. 
"""


class Snake(object):
    """ 뱀 클래스 """
    color = GREEN  # 뱀의 색

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]  # 뱀의 위치
        self.direction = 'north'  # 뱀의 방향

    def draw(self, screen):
        """ 뱀을 화면에 그린다. """
        for position in self.positions:  # 뱀은 여러개의 블록으로 이루워져있어 for문으로 순회하며 그리도록함
            draw_block(screen, self.color, position)
    # pass


class Apple(object):
    """ Apple 클래스 """
    color = RED  # 사과 색

    def __init__(self, position=(5, 5)):
        self.position = position  # 사과 위치

    def draw(self, screen):
        """사과를 화면에 그린다."""
        draw_block(screen, self.color, self.position)

    # pass


class GameBoard(object):
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
    # pass