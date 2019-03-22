# Str08.py


# a1 a2  a3   a4;print(a1, a2, a3, a4) --> Java, C, SQL, Python
a1, a2, a3, a4 = 'Java,C,SQL,Python'.split(',')
print(a1, a2, a3, a4)

b = ['H', 'e', 'l', 'l', 'o']
b = ''.join(b)
print(b)

a = ''
for i in range(0,len(b)):
    a += b[i]

print(a)



print('안녕하세요', sep=' ', end='\n')
print('안녕하세요', end='')
print('안녕하세요', end=' ')
print('안녕하세요')
print('안','녕','하','세','요', sep=' ')
print('안','녕','하','세','요', sep='/')
print('안','녕','하','세','요', sep=',', end='\t')
# sep는 그 구문 내에서의 구분자, end는 복수개의 구문 사이의 구분자


