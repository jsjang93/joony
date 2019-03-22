# Func11.py


def calc(n,m):
    a = n+m
    b = n-m
    c = n*m
    d = n/m
    return a, b, c ,d

print(calc(20, 10))
a,b,c,d = calc(20,10)
print(a,b,c,d)


def swap(a,b):
    return b,a

x = 200
y = 100
x, y = swap(x,y)
print(x,y)



 

