#Test02.py

a = 10
print(a, type(a), id(a))

b = 'Hi'
print(b, type(b), id(b))

b = 3.14
print(b, type(b), id(b))

b = True
print(b, type(b), id(b))

b = 3+4j
print(b, type(b), id(b))

b = [10, 20, 30]
print(b, type(b), id(b))

a = 4
b = 10
c = a+b
print(c, type(c), id(c))

b = 10
c = [10,20,30]
print(a, type(a), id(a))
print(b, c[0])
print(id(b), id(c[0]))
# python은 참조형 변수만 존재. 변수에는 항상 주소값 저장
# 변수이름은 달라도 주소가 가리키는 값이 같으면 같은 주소 할당
# 그래서 느리다.(메모리에 기존 값이 있는지 찾아야한다.)

d = (10, 20, 30); print(type(d))
e = {10, 20, 30}; print(type(e))
f = None; print(type(f))






