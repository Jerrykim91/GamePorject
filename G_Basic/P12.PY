# 함수
a = 10
def test():
    # 함수 내부에서 사용하는 변수는 함수를 떠나면 종료 : 지역변수
    a = 11
test()
print( a )