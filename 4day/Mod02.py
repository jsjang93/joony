# Mod02.py
# <-- /MyCalc02 / ~~~


print('name: {0}'.format(__name__))

#from MyCalc02 import Sum00, Sub00
from MyCalc02 import * # *은 __init__.py안의 __all__을 참조해서 호출

x = 2000; y = 1000
Sum00.Sum(x,y)
Sub00.Sub(x,y)

