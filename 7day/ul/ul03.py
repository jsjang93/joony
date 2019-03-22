# ul03.py
from bs4 import BeautifulSoup
f1 = open('web/Test01.html','r',encoding="utf-8")
bs = BeautifulSoup(f1,"html.parser")

bsList = bs.find_all("p") # p tag만 가져옴
#print(bsList)
#for bs in bsList : print(bs)
#print(bsList[1])
#a = bs.find("head")
#print(a)
#print(a.find("title"))
b = bs.find("head").find("title"); print(b)


f1.close()