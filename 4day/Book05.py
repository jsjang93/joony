# Book05.py
# static : 어디서나 접근가능, class : 같은 모형인애들만 접근가능, instance : 개별공간

class Book():
    category = '소설'               # class 멤버 속성

    def __init__(self):
        self.title = '무제'         # instance 멤버 속성

    def pBook(self):
        print(self.title)           # instance 멤버 메소드

    @ classmethod                   # class 공용 공간(class 메소드)이라고 선언해줌
    def pCate(cls):                 # self가 들어가면 다 instance, cls로 꼭 쓸필요는 없지만 관용적으로 cls(class)의 약자를 쓴다
        print(Book.category)        # class 멤버 메소드

    @ staticmethod                  # static 메소드라는 정의
    def test():
         print("이것은 static 멤버 메소드")

a = Book()
a.pBook() # 무제
a.pCate() # 소설
a.test() # 이것은 static 멤버 메소드

########################################################################################################################

# instance한 애들
b1 = Book(); b2 = Book()
print(b1.title, b2.title)
b1.pBook(); b2.pBook() # Book.pBook()은 불가능함

# class한 애들
print(Book.category, b1.category, b2.category)
Book.category = '수필' # 다 같이 바뀐다
Book.pCate(); b1.pCate(); b2.pCate()

# 어디서나 호출 가능
Book.test(); b1.test(); b2.test()






















