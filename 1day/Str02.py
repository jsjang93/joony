# Str02.py




b = 20; c = 10;
print(b+c) # 30
print(str(b)+str(c)) #2010





a = 'Welcome to HPEducation'
print(a[:7])
print(a[3:10])
print(a[11:])
print(a[-11:])
print(len(a))
print('HP' in a)

print('==========')
print('='*10)

for i in range(0,10):
    print('+', end = '')
print()


print('==========')
print('='*10)

b = a.split( )
print(b[0])

c = a.split('c')
print(c)

import re
re_a = re.sub('c', '*c', a)
print(re_a.split('*'))


