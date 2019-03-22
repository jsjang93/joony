# List01.py
# ArrayList -> List(R, Python, Scratch)


a = ['딸기', '당근', '수박']
print(a, type(a))

a += ['참외']
print(a)

a = a + ['메론']
print(a)

a += [10] # 10 아니라 [10]으로 저장해야됨 + 기호는 양쪽 타입 동일
print(a, type(a[5])) # 10은 int로 저장


b = [10,'A',"안녕", True, 3.14, [10, 20, 30]]
print(b)
print(b[0] == b[-1][0])
print(id(b[0]) == id(b[-1][0]))


c = ['강', 10, 3.14, True, None, a] # NULL data 저장용
print(len(c)) # None도 센다
print(c)
