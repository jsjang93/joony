# Func07.py




def pSum(mod, *n):
    ans = 0
    for i in n:
        ans += i
    return mod + " " + str(ans)



print(pSum('덧셈',20,10)) # 덧셈 30
print(pSum('덧셈',20,10,5)) # 덧셈 35
print(pSum('덧셈',20,10,5,2)) # 덧셈 37

a = [10,20,30,40,50]
print(pSum('덧셈', *a)) # 덧셈 150


