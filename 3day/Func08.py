# Func08.py


a = 7
def Sum(*n):
    global a
    for i in n:
        a += i
    return a
print(Sum(20,10))

print("="*50)

b = 0
def test(n):
    global b
    b = n
    return b
test(200)
print(b)


