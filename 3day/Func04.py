# Func04.py




def Sum(*n1):
    ans = 0
    for i in n1:
        ans += i
    return ans



print(Sum(20,10))
print(Sum(20,10,5))
print(Sum(20,10,5,3))


b = [10, 20, 30, 40, 50]
print(Sum(*b)) # <--- *를 같이치면 됨


def sum(n1):
    ans = 0
    for i in n1:
        ans += i
    return ans


print(sum(b)) # <--- sum은 매개변수에 *이 없어서








