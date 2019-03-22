# Ani02.py - Python은 다중상속을 허락한다.


class A:
    def test1(self): print('A')
    def testA(self): print('TestA')

class B:
    def test1(self): print("B")
    def testB(self): print("TestB")

class C:
    def test1(self): print("C")
    def testC(self): print("TestC")


class D(A,B,C): pass


d1=D()
d1.test1() # 겹치는건 제일 첫번째것으로
d1.testA(); d1.testB(); d1.testC()










