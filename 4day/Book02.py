# Book02.py


class Book():
    def __init__(self,  title = '무제', author = '미상', price = 0):
        self.title = title
        self.author = author
        self.price = price

    def pBook(self):
        print(self.title, self.author, self.price) # instance 멤버 메소드


b1 = Book()
b2 = Book()
b3 = Book()
b4 = Book()

b1.pBook()
b2.pBook()
b3.pBook()
b4.pBook()

b1 = Book()
b2 = Book('파이썬')
b3 = Book('자바','이승엽')
b4 = Book('DB','김연아',30000)

b1.pBook()
b2.pBook()
b3.pBook()
b4.pBook()


b = [b1, b2, b3, b4]
for i in b:
    print(i.price)





