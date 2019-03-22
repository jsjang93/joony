# File04.py

# 1. open() read() ==> 한줄로 쭉 연결된 str
file1 = open('./Users/users01.txt','r')
users1 = file1.read()
print(type(users1))
print(users1)
file1.close()

print("="*20)

# 2. open() readline() ==> 줄별 str
file2 = open('./Users/users01.txt','r')
while True:
    users2 = file2.readline()
    if not users2 : break   #<-- ''
    print(type(users2),users2)
file2.close()

print("="*20)

# 3. open() readlines() ==> list
file3 = open('./Users/users01.txt','r')
users3 = file3.readlines()
print(type(users3))
print(users3)
for u in users3 : print(type(u),u)
file3.close()

