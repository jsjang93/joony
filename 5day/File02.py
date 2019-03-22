# File02.py
# open(), 처리(): write(), read(), close(): 메모리에 파일 내리기 - 필수

# f1 = open()
# 미리 f1.close()를 적고 시작

user = 'Hong'

f1 = open('./Users/users01.txt', mode = 'a', encoding = 'cp949') # w: 신규 - 기존 같은 이름 데이터 있다면 다 지워짐.. 주의!, a : 추가
f1.write('\n' + user)
print("추가완료") # 읽혀진다

f2 = open('./Users/users01.txt', mode = 'r', encoding = 'cp949') # w: 신규 - 기존 같은 이름 데이터 있다면 다 지워짐.. 주의!, a : 추가
user = f2.read()
print(user)
f1.close()
f2.close()
print("추가완료") # 읽혀진다

##################################################################

f2 = open('C:/PySrc/5day/Users/users02.txt', mode = 'a', encoding='utf-8')
f2.write('\n' + user)
f2.close()
print("추가완료")
