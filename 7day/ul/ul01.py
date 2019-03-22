# ul01.py
from bs4 import BeautifulSoup
f1 = open('HTML/Test00.html','r',encoding="utf-8")
#fdata = f1.read()
bs = BeautifulSoup(f1,"html.parser") # html.parser, xml.parser

# print(fdata)
print(bs, type(bs))
print(bs.prettify(), type(bs.prettify())) # 얘는 html 문법까지 이해해서 왔다 - tag
f1.close()


