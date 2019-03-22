# Ani03.py



class Animal:
    def __inint__(self): # 생성자 메소드 오버라이드
        self.name = '이름'
    def __add__(self, other): # 산술 덧셈 연산자 메소드 오버라이드
        return self.name + ', ' + other.name +' ' + "입니다."


class Dog(Animal): pass
class Cat(Animal): pass

d1 = Dog(); c1 = Cat(); d1.name='아치'; c1.name = '해피'
print(d1.name + c1.name)

a1 = Animal()
print(d1 + c1)




