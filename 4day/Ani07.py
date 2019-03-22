# Ani07.py - 같은 이름의 메소드를 편리하게 호출

from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def cry(self): pass

class Dog(Animal):
    def cry(self): print('멍멍')
class Cat(Animal):
    def cry(self): print('야옹')
class Duck(Animal):
    def cry(self): print('꽥꽥')

aList = [Dog(),Cat(),Duck()]
for c in aList : c.cry()
