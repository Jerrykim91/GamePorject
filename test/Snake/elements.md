## 개체 정의 (클래스)
```py 

Machine  
class Machine:
	“””Machine 클래스”””
	pass

Worker
class Worker:
	“””Worker 클래스”””
	pass

Load 
- 배열로 표현(0,1)
- 1은 이동할수 있는 칸 , 0 은 이동할수 없는 칸으로 나타냄 
class Load :
	“””Load  클래스”””
	pass

Site
class Site:
	“””Site 클래스”””
	pass
```

## 속성정의 (클래스 속성) 

**Worker**
- Location
- Movement(Direction of movement)

**Vehicle**
- Location
- Direction of movement
- Horizontal / vertical size

**Machine**
- Location
- Horizontal / vertical size


**Site**
- Horizontal / vertical size
- Vehicle Location
- Machine Location
- Worker Movement

## 개체의 동작정의 (메서드 정의 )

**Worker**
- Move randomly

**Vehicle**
- Move in one direction
- Situation judgment
- Send and receive signal

**Machine**


**Site**


