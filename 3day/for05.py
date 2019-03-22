# for05.py
'''
1: *
2: **
3: ***
4: ****
5: *****
'''

for i in range(1,6):
    print("{}: {}".format(i, "*"*i))


print("===========================")

for i in range(1,6,1):
    print(i, end=': ')
    for j in range(1, i+1):
        print('*', end='')
    print()

print("===========================")
          
for i in range(1,21):
    print("{}".format(i), end=' ')
    if i%5==0:
        print()

print("===========================")


m=0
for i in range(1, 5):
    for j in range(0, 5):
        print("{}".format(i+j+m), end='\t')
    print()
    m += 4


















