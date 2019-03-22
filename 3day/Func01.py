# Func01.py

# 함수(메소드) - 입력, 반환, 처리, 이름





def hello():     #  <----  hello는 주소다.
    a = input("이름은?")
    print('{}님 안녕하세요'.format(a))

def Hi(name):
    print(name + '안녕하세요')
    return "Hello"

print(Hi('Tom'))
#hello()

def 덧셈(a,b):
    return a+b

ans = 덧셈(20,10)
print(ans)

a = Hi
a('Jane')

b = 덧셈
print(b(300,200))

