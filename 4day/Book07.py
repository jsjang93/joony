# Book07.py

class Book :
    def __init__(self,t,a,p):
        self.__title__ = t # public
        self.__author_ = a # private --> 메소드 우회접근
        self.__price = p   # private --> 메소드 우회접근
        self.category = '' # 방치 (public)

    def pBook(self):
        print(self.__title__+','+self.__author_+','+str(self.__price))
    def setTitle(self,t): self.__title__ = t
    def setAuthor(self,a): self.__author_ = a
    def getAuthor(self): print(self.__author_)
    def setPrice(self,p): self.__price =p

b1 = Book("파이썬","홍길동",30000)
b1.pBook()
b1.setAuthor("김연아"); b1.getAuthor()

