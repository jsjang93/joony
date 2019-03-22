# Dict02.py

a = {'사과' : 'apple',
     '포도' : 'grape',
     '바나나' : 'banana',
     '컵' : 'cup',
     '물' : 'water'}

a['강'] = 'river'
print(a)

a['자바'] = 'Java'

a.pop('강') # 강 지우기
print(a)

del a['자바']
print(a) # 자바 지우기



# keys에서 바나나가 존재하는지 궁금
print("바나나" in a)

# values에서 grape 존재하는지 궁금
print('grape' in a.values())

# items에서 '사과', 'apple' 존재하는지
print(('사과', 'apple') in a.items())
print('사과' in a.keys(), 'apple' in a.values())
print(a.items())


print(a['포도'])
print(a.get('포도')) # <-- key에서만 사용 가능

print(a.get('grape'))
print(a.get('grape', '없음')) 


# 강 river
a['강'] = 'river'
print(a)

b = {'불' : 'fire', '집' : 'house'}
# print(a+b) <-- error

a.update(b) # a에다가 b를 추가
print(a)


# 없으면 추가, 있으면 "기존 data" 반환
# 집 home, 책 book
a.setdefault('집','home')
a.setdefault('책','book')
print(a)


for z in a.items():
    print(z)

y = list(a.items()) # list로 전환; element는 tuple
print(y)




# 키로 밸류 호출
'''
q = input("찾는게 뭐야\n")
for i, item in enumerate(a.items()):
    if item[0] == q:
        print(item[1])
        break
    if (i+1) == len(a.items()):
        print("그런거 없어")
'''

q2 = input("찾는게 뭐야\n")
a_rev = {v:k for k,v in a.items()}
try:
    print(a_rev[q2])
except:
    print("Nope!")






















