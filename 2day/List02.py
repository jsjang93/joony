# List02.py

a = [10, 20, 30]
print(len(a), a)

a.append(20)
print(a, a.count(20), len(a))

a.insert(1, 50)
print(a)

a.pop()
print(a)

a.append(20)
a.remove(20) # 앞에 있는 것이 빠짐
print(a)

a.extend([50, 60]) # 여러개 한번에 넣기
print(a)


a += [70, 80]
print(a)

print(a.index(20))

a.pop(-3) # 뒤에서 3번째거 빠짐
print(a)





