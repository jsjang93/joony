# Ani01.py
# ---> 개 Dog, 고양이 Cat


class Animal: # 모든 class의 최상위 부모 class는 Object
    def __init__(self):
        self.name = '이름'
    def cry(self): return '울음소리'
    def shout(self): return '으르렁'


class Dog(Animal):
    def __init__(self, name = '몽몽이'):
        self.name = name
    def cry(self): return '몽몽' # 메소드 오버라이드

class Cat(Animal):
    def __init__(self):
        self.name = '냥냥이'
    def cry(self): return '냥냥' # 메소드 오버라이드

class Turtle(Animal):
    def __init__(self):
        self.name = '메이'





d1 = Dog(); c1 = Cat(); t1=Turtle()
d1.name = '별이'; c1.name = '솜이'
print(d1.name, d1.cry(), d1.shout())
print(c1.name, c1.cry(), c1.shout())
print(t1.name, t1.cry(), t1.shout())

d2 = Dog("지니")




