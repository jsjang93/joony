# File05.py
uList = ['Hong','James','Tom','Alice','Jane']
# /Users/users03.txt
# open(w), write(), close()
f1 = open('./Users/users03.txt', mode = 'w', encoding = 'cp949')
# 1: Hong\n , 2: James\n + 3: Tom\n + 4: Alice\n + 5: Jane\n


i = 0
for u in uList:
    i += 1
    f1.write("{}: {}\n".format(i, u))



f1.close()
if f1.closed : print("입력 완료")
