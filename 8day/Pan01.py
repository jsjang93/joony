# Pan01.py
# Pandas 라이브러리 : Data 분석 라이브러리
#       - Data Frame (Series) <-- List, Dict , Array
# Pandas : 코딩하는 엑셀
import pandas as pd

# Series
a = [3,5,-1, 4]
s1 = pd.Series(a)
print(s1,type(s1))
print(s1.index)

b = ['A','B','D','C']
s2 = pd.Series(a,index=b)
print(s2,type(s2),s2.dtype)
print(s2.index)

c = {'Jane':80,'Tom':70,'Alice':90,'John':60}
s3 = pd.Series(c)
print(s3,type(s3),s3.dtype)
print(s3.index)

s3.name = 'StuPoint'
s3.index = ['제인','톰','앨리스','존']
s3.index.name = '이름 ' #'Name'
print(s3)

d = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}

#s4 = pd.Series(d)
#print(s4)

df1 = pd.DataFrame(d)
print(df1)
print(df1.index)
print(df1.columns)
print(df1.values)

df1.index = ['학생1','학생2','학생3','학생4']
df1.index.name = ['학생이름']
df1.columns.name = ['정보']
print(df1)
print(df1.index)
print(df1.columns)

########################################
e = [['Jane',34,80],
     ['Tom',27,70],
     ['Alice',51,90],
     ['John',45,60]]
print(e)
df2 = pd.DataFrame(e,columns=['이름','나이','점수'],
                   index=['학생1','학생2','학생3','학생4'])
print(df2)

########################################
import numpy as np
f = np.random.randn(4,3) ; print(f)
df3 = pd.DataFrame(f) ; print(df3)
df3 = pd.DataFrame(f,columns=['A','B','C']) ; print(df3)

g = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
print(g)
df4 = pd.DataFrame(g,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])
print(df4) # NaN : Not a Number (Null)

df5 = pd.Series([1,2,3,np.nan,5,6])
print(df5)





