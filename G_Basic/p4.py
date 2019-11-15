'''
> 딕셔너리 : {} ->  , 
  순서 X, 키:값, 키는 중복되면 X, 값 중복 ok
  => 테이블상의 한개의 row, json의 객체 , js의 객체와 동일
'''
# 이 스타일을 가장 많이 사용
dic = {}
print( dic, len(dic), type(dic))
dic = dict()
print( dic, len(dic), type(dic))
######################################################
# 키를 통해서 값을 이해할수 있다. 직관적으로
dic = {
    'name':'홍길동',
    'age':100
}
print( dic, len(dic), type(dic))
# 인덱싱 : 순서가 없으므로, 데이터를 특정할수 있는 키값을 사용한다
print( dic['name'] )
# 데이터추가, 키는 모든지 올수 있다 2는 인덱스가 아닌, 키를 의미
dic[2]='hello'
print( dic, len(dic), type(dic))
print( dic[2] )
########################################################################
print( dic.keys() )
print( dic.values() )
# 키 조사
print( 'name' in dic )
# for으로 돌려보기 => for 에서 확인

