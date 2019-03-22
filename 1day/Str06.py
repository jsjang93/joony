# Str06.py

a1 = 'Welcome to Korea Education'
a2 = 'Welcome to Korea Education'

print(id(a1) == id(a2))
print(a1 is a2)
print(a1 == a2)

print(id(a1) is id(a2))


print('skhi 입력 바람')
b1 = 'skhi'
b2 = input()
b3 = 'skhi'
b4 = b1
b5 = b1[:] # string만 -- seq. data 에서는 다름
print(b1 == b2, b1 is b2, id(b1), id(b2))
print(id(b5), id(b3), id(b4), id(b1))
# 값은 같으나 주소가 다르다. --> input 함수 실행시 이미 메모리 할당
# data 크롤링하고 나서 똑같은 data라도 같은 개체로 볼 수 없다.







