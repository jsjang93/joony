# Func05.py
def pList(*x) :
    for i in x: print(i, end=' ')
    print()

a = [10,20,30,40,50]
b = [11,22,33]
c = (1,2,3,4)
d = {12,23,34,45,56,67}

pList(a) # <--- list전체를 한 묶음으로 본다.
pList(*b)
pList(*c)
pList(11,22,33)
pList(*[11,22,33])

def Calc(a,b,c):
    if a == 'Sum': print(b+c)
    elif a == 'Sub' : print(b-c)

Calc('Sum',20,10) # 30
Calc('Sub',60,15) # 45












