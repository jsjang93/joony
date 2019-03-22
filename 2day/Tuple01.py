# Tuple01.py
# data 수정 불가

a = (1, 2, 3)
print(type(a), a, a[1])
# a[1] = 200 --> 얘는 안됨

b = (10,)
c = 10,
d = 'A', 'B', 'C'
e = 'A',
f = 10,20,30
g = 10,20,
print(b, c, d, e, f, g)
# 에러 없, 다 튜플타입

x1 = (10)
x2 = 10,
x3 = (10,)
print(type(x1), type(x2), type(x3))
# x1만 int형

h = [10],
print(type(h))
# 튜플

m = (11,22,33,)
print(m[1])
print(len(m))

x = 11; y=11,
print(type(x) == type(y), type(y))












