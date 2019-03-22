# Tuple03.py

a = '사과', '배', '토마토';
# a[1] = '포도' <-- 에러

b,c,d = a # Tuple Unpacking
print(a, id(a))
print(b, c, d) # <-- 주소 이전의 개념

c = '포도'
a = b,c,d # Tuple Packing
print(a, id(a))

z = 10, 20, 30
# z의 모든 숫자를 1씩 증가 시켜라

z0, z1, z2 = z

z = z0+1, z1+1, z2+1
print(z)

z = z[0]+1, z[1]+1, z[2]+1
print(z)


z = str(z[0]) + 'a', str(z[1]) + 'b', str(z[2]) + 'c'
print(z) # '12a', '22b', '32c'
# z1,z2,z3 = map(str,z) <-- 한번에 str로 전환됨


z_li = list(z)
z_li[0] = 100
print(z_li)
# list로 바꿔서 수정이 가능








