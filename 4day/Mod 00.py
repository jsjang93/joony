# Mod00.py


print('name: {0}'.format(__name__))


import Calc00
import Calc00 as c # c로 쓰겠다
from Calc00 import * # c조차도 안쓰겠다

x = 20; y = 10;
Calc00.Sum(x,y)
c.Sub(x,y)
Mul(x,y)

import sys
for path in sys.path:
    print(path)         # 따로 디렉토리를 설정하지 않아도 자동으로 참조하는 디렉토리