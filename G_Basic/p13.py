# class 
# 파이썬에서 자기 자신 객체를 가르키는 키워드 self
# self => python, objective-c
# this => java, js, 대다수 랭귀지
class Person:
    '''
    맴버 변수
    '''
    name   = None
    age    = 0
    weight = 0
    '''
    맴버 함수
    '''
    def eat(self, food):
        print( '%s를 먹는다' % food )
    '''
    생성자 : 객체를 생성하고, 맴버변수를 초기화 하는데 목적
    '''
    def __init__(self, name, age, weight):
        # 클레스 내부에서 맴버들을 접근할때, self.맴버(변수/함수)
        self.name   = name
        self.age    = age
        self.weight = weight
        # 부모 생성자 호출
        #return super().__init__()
    '''
     객체를 설명하는 코드를 구현현 된다. 통상 문자열로 구성
     맴버 변수값이나 상태를 표현한 정보가 들어가면  OK
     자바의  toString()의 맥락과 유사
    '''
    def __repr__(self):
        return '''
            name=%s age=%s weight=%s
        ''' % (self.name, self.age, self.weight)

# 객체 생성
obj = Person('품질', 1, 2)
print( obj )
obj.eat('1')

# 상속
# 부모의 모든것을 가지고, 재정의할수 있고, 추가할수 있다
class XMan(Person):
    # 맴버 변수 추가
    abil = 100
    # 맴버 함수 추가
    def speed(self):
        print('시속 500km로 달린다')
    # 재정의 (내용 구성이 달라진다 부모대비) : overriding
    def eat(self, food):
        print( '%s를  1초만에 먹는다' % food )
    # 생성자도 확장()
    def __init__(self, name, age, weight, abil):
        #  부모 생성자를 이용한 맴버변수 초기화
        super().__init__(name, age, weight)
        self.abil = abil

mu = XMan( '로건', 200, 100, 103)
mu.speed()
mu.eat('닭가슴살')
print( mu )
