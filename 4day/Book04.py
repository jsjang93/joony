# Book04.py

class Book():
    category = '소설'


b1 = Book(); b2 = Book()
print(b1.category); print(b2.category); print(Book.category)

b2.category = 'it'
print(b1.category); print(b2.category); print(Book.category)

Book.category = '수필'
print(b1.category); print(b2.category); print(Book.category)





