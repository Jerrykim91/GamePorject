'''
연속데이터(시퀀스 타입)
set() -> 중복제거 후 리스트로 변환해서 처리
- 교집합, 합집합, 차집합 => 느려서!! => pandas에서 해결 
- 순서없음, { 값, 값, 값, .. } => 중복제거 리스트 변경 처리
'''
a = 'helloworld'
# 중복제거
b = set( a )
print( b )
# 리스트 변환
print( list(b) )
#########################################################
# 합집합, 차집합(방향성,  A-B, B-A),  교집합
a = set( [1,3,5,7,9,2,6,5] )
b = set( [2,4,6,8,1,5,4] )
# 교집합
print( a.intersection(b) )
# 합집합
print( a.union(b) )
# 차집합
print( a.difference(b) )
print( b.difference(a) )