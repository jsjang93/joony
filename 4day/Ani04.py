# Ani04.py

class Animal:
    def __init__(self):
        self.name = '무명'
        print("Animal 실행"+ self.name)
class Dog(Animal):
    def __init__(self):     # 생성자 메소드 오버라이드
        
        print("Dog 실행")

d1 = Dog()