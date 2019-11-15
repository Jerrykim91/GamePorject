# 예외처리
#   > 풀코드 형태 확인
try:
    print(1)
    #print(1/0)
    print(2)
except Exception as e: # 예외가 발생하면 진입
    print(3, e)
else:    # 예외가 없으면 진입
    print(4)
finally: # 무조건 마지막으로 진입
    print(5)
