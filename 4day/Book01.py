# Book01.py

'''

class
    member field
    member method


'''


# 서점사장: '시스템으로 만들어줘~'
# 서점: 책(제목, 저자, 가격)

class Book():
    def __init__(self): # member 생성자  <-- 메모리에 로드, 호출
        self.title = '무제' # instance 멤버 속성
        self.author = '미상'
        self.price = 0

    def pBook(self):
        print(self.title, self.author, self.price) # instance 멤버 메소드




b1 = Book()
b1.pBook()
b1.title = 'Python';b1.author = 'Tom';b1.price = 30000
b1.pBook()
b2 = Book()
b2.title = "Java";b2.author = 'Jane';b2.price = 20000
b2.pBook()

print(id(b1), id(b2))

