# Set01.py
# 중복불가, 집합 개념 

a = {}      # dict
print(a,type(a))

b = {10,20,30} # set 
c = {10:'사과'}# dict
print(type(b),type(c))

과일 = "사과","배","토마토","배","토마토","포도"
print(type(과일))
fruits = set(과일)

print(type(fruits),fruits)
과일 = list(fruits)
과일.sort()
print(type(과일),과일)

과일2 = "사과","배","토마토","배","토마토","포도"
과일2 = list(set(과일2))
과일2.sort()
print(과일2)


 

