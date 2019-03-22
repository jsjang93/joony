# File06.py
# 1회성 읽기 : with ~~ as --> open() , close()


with open('./Users/users03.txt','r') as file:
    users = file.read()
    print(users)

