# Func20.py - Closure

def Calc():
    def sum(i,j): return i+j
    def sub(i,j): return i-j
    def mul(i,j): return i*j
    def div(i,j): return i/j
    def ans(x,a,b):
        if x =='덧셈': return sum(a,b)
        elif x =='뺄셈': return sub(a,b)
        elif x =='곱셈': return mul(a,b)
        elif x =='나눗셈': return div(a,b)
        
    return ans

계산 = Calc()
print(계산('덧셈',30,12))
print(계산('뺄셈',30,12))
print(계산('곱셈',30,12))
print(계산('나눗셈',30,12))

