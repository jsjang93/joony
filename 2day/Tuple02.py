# Tuple02.py

a = (10, 20, 30, 40, 50)
b = 60, 70
c = 80,
print(a + b + c)
# a b c는 다 투플

print((a+b+c)[1:-1])
print(type(a+b+c))

d = (10,20,30),90,'A',(40,(50,[60,70],80),100),
print(d)
# d의 타입 : 투플
# d의 길이 : 4
print(d[3][1][1][1])
# d : 70 출력

b = True,
print(type(b), b, len(b))
b = None,
print(type(b), b, len(b))
b = None, None
print(type(b), b, len(b))

