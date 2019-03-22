# Str05.py

a1 = 'Welcome to '
a2 = 'Korea Education'

print(a1 + a2)

s1 = a1[3:] + a2[:5]
print(s1)

s2 = a1.split()[0][3:] + ' ' + a1.split()[1]+ ' ' + a2.split()[0]
print(s2)

s3 = a1 + a2
print(s3[3:16])
# come to Korea

n1 = 'four'
b = 'I have %s apples' %n1
print(b)

n1 = input("수를 입력하세요\n")
print('I have {} apples'.format(n1), type(n1), type(print(1)))


s2 = 4; s3 = 'five'
c = 'I have %d apples and %s bananas' %(s2, s3)
print(c)

print('I have {} apples and {} bananas'.format(s2, s3))


e = 'hi'
print('안녕 {} 제인'.format(e))
print('안녕 %10s 제인' %e)
print('안녕 %-10s 제인' %e)


f = 12.345678
print('안녕 %d 제인' %f)
print('안녕 %f 제인' %f)
print('안녕 %10f 제인' %f)
print('안녕 %-10f 제인' %f)
print('안녕 %10.4f 제인' %f)
print('안녕 %-10.4f 제인' %f)

이름 = '홍길동'
print(이름)






















