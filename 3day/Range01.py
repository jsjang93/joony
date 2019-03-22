# Range01.py





a = [0,1,2,3,4,5,6,7,8,9]
b = [i for i in range(1,11)]


print(a == b)
print(b, type(b), b[1])

c = [i for i in range(0,11,2)]
print(c)


d = [i for i in range(10,0,-1)]
print(d)


f = a[1::2]
print(f)

e = [i for i in b if(i%2)==1]
print(e)
# DBMS랑 비슷
# Select 항목 From 대상 Where 조건
# for    항목 in   대상 if    조건




g = [i**2 for i in a if(i%2)==1]
print(g, type(g))

h = {i:(i**2) for i in a if(i%2)==1}
print(h, type(h))


x = 'ereefaerwthrtehberewfcredfdf'
# y = [x에서 'a','b','c' 가 아닌 문자] 중복제거 후, 정렬

x1 = x.split('a')
x2 = ''.join(x1)
x3 = x2.split('b')
x4 = ''.join(x3)
x5 = x4.split('c')
x6 = ''.join(x5)
x7 = set(x6)

y = sorted(x7)
z = sorted(set([i for i in x if i not in 'abc']))
print(y)
print(z)










