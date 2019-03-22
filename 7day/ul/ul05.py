# ul05.py
# Test02.html
# --> body
from bs4 import BeautifulSoup
import re

from bs4 import BeautifulSoup
import re

f1 = open("web/Test02.html","r",encoding='utf-8')
bs = BeautifulSoup(f1,"html.parser")
tags1 = bs.find_all(re.compile("^p")) # ^p는 p로 시작하는 애들
tags2 = bs.find_all(align="center")
print(tags1)
print("=============================")
print(tags2)
f1.close()