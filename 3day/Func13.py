# Func13.py - lambda식





def sum(i,j): return i+j
def sub(i,j): return i-j
def mul(i,j): return i*j
def div(i,j): return i/j
def nmj(i,j): return i%j

a = sum
print(a(20,10))

# 람다식 input1,input2, ....: return값
b = lambda i,j:i%j
print(b(32,5))



calcList = [sum, sub, mul, div, b, lambda i,j:i*j]
for c in calcList:
    print(c(200,100))

print("="*30)

calcList2  = []
calcList2.append(sum)
calcList2.append(mul)
for c in calcList2: print(c(2000,1000))
print("="*30)
calcList2.remove(mul)
for c in calcList2: print(c(2000,1000))


사칙연산 = {'덧셈':sum, '뺄셈':sub}
print(사칙연산['덧셈'](20,10))








