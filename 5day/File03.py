# File03.py


user = 'Ali'
f1 = open('./Users/users01.txt', mode = 'a+', encoding = 'cp949') # a+ : 읽기와 쓰기 같이
users1 = f1.write('\n' + user)
f1.seek(0)  # 커서의 위치변경
users1 = f1.read()
print("닫힘" if f1.closed else "안닫힘")
f1.close()
print("닫힘" if f1.closed else "안닫힘")
print(users1)
