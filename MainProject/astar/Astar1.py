# 엑셀파일 명과 경로, 시작점과 끝점은 바꿔주셔야 정상적으로 작동

import csv


class Point:  # "Point" 클래스 생성
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.gScore = 0
        self.hScore = 0
        self.fScore = 0

    def __eq__(self, other):
        return self.position == other.position


def get_start_point(position):
    point = Point(parent=None, position=position)

    point.gScore = 0
    point.hScore = 0
    point.fScore = 0

    return point


def get_end_point(position):
    point = Point(parent=None, position=position)

    point.gScore = 0
    point.hScore = 0
    point.fScore = 0

    return point


# A-star 알고리즘 구현
def astar(maze, start, end):
    # 시작점, 도착점 정의
    start_point = get_start_point(start)
    end_point = get_end_point(end)

    opened_list = []
    closed_list = []

    opened_list.append(start_point)  # 시작점을 열린 목록에 추가

    # 열린 목록이 모두 비어있을 때까지 아래를 반복함
    while opened_list:
        this_point = opened_list[0]

        # 가장 작은 f(x)값을 가지는 노드를 찾아냄
        for element in opened_list:
            if element.fScore < this_point.fScore:
                this_point = element

        opened_list.remove(this_point)
        closed_list.append(this_point)

        # 탐색중인 지점이 도착점이라면 멈추고 길을 출력함
        if this_point == end_point:
            path = []
            get_path_point = this_point

            while get_path_point is not None:
                path.append(get_path_point.position)
                get_path_point = get_path_point.parent

            return path[::-1]

        # 상하좌우, 총 4개의 점을 탐색함(f(x)비용을 구함)
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            point_position = ((this_point.position[0] + new_position[0]), (this_point.position[1] + new_position[1]))
            print(len(maze))
            if (point_position[0] < 0) or (point_position[1] < 0) or (point_position[0] > len(maze) - 1) or (point_position[1] > len(maze[0]) - 1):
                print(point_position[1] > len(maze[len(maze) - 1]) - 1)
                continue

            # 탐색중인 지점이 갈 수 없는 곳이라면 무시
            if maze[point_position[0]][point_position[1]] != "":
                continue

            new_point = Point(parent=this_point, position=point_position)

            # 탐색중인 지점이 이미 닫힌 목록에 있다면 무시
            if new_point in closed_list:
                continue

            # 탐색중인 지점의 f(x), g(x), h(x) 값 구하기
            new_point.gScore = (this_point.gScore + 1)
            new_point.hScore = (((point_position[0] - end_point.position[0])**2)**0.5) +\
                               (((point_position[1] - end_point.position[1])**2)**0.5)
            new_point.fScore = (new_point.gScore + new_point.hScore)

            for element in opened_list:
                if (new_point == element) and (new_point.gScore > element.gScore):
                    continue

            opened_list.append(new_point)


maze1 = []

# 엑셀 파일을 사용해 맵 데이터를 읽어옴
with open("map01.csv", "r") as reader:
    for line in reader:
        maze1.append(line.strip().split(","))

# 시작점과 도착점 정의
start1 = (3, 35)
end1 = (24, 56)

# A-star 알고리즘 실행
path = astar(maze1, start1, end1)

for point in path:
    maze1[point[0]][point[1]] = 2

# A-star 알고리즘 결과를 바탕으로 최적경로를 엑셀에 표시
with open("map.csv", "w", newline="") as reader:
    wr = csv.writer(reader)

    for line in maze1:
        wr.writerow(line)
