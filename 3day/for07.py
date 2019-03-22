# for07.py

a = [10,20,30,40,50]

for i in a : print(i)

for i in range(len(a)) : print(a[i])

print()
print("="*40)

######################

# 1 : 10

print("1번 방법")
for i in range(len(a)):
    print("{}: {}".format(i+1, a[i]))
    

print()
print("="*40)

print("2번 방법")
for i,v in enumerate(a):
    print("{}: {}".format(i+1, v))




