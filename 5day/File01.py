# File01.py
# open(), 처리(): write(), read(), close(): 메모리에 파일 내리기 - 필수

# f1 = open()
# 미리 f1.close()를 적고 시작

f1 = open('./Users/users01.txt', mode = 'r', encoding = 'cp949') # 상대경로
users1 = f1.read()
f1.close()
print(users1) # 읽혀진다

##################################################################

f2 = open('C:/PySrc/5day/Users/users02.txt', mode = 'r', encoding='utf-8') # 절대경로; 똑같이 생겼는데 안읽힌다. - 인코딩방법이 달라서 그럼. --> option에 utf-8로 인코딩하라고 명령
users2 = f2.read()
f2.close()
print(users2)
