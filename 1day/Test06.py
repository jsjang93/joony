# Test06.py


import time, sys

time.sleep(1)

    
c = b = a = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))


e = 11; f = 12; g = 13;
print(e, f, g)

# print 함수 내에서 콤마는 복수 주소값을 가지고

h = e,f,g = 11,12,13
print(e,f,g, h, type(e), type(f), type(g), type(h))


h = 33
print(h, id(h))
h = None # 변수와 주소 값의 연결을 파괴
print(h, id(h))
del h  # 변수명 자체도 파괴
# print(h, id(h)) - 에러

