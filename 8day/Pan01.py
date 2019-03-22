#pan01.py
import pandas as pd
# Quiz 2) 학생들의 국어점수가 70 이상이면 '합격', 아니면 '불합격'
c = {'Tom':90,'Jane':60,'Alice':70, 'JOhn': 80}
s3 = pd.Series(c)
print(s3,type(s3))
print(s3.index)
print(s3.values)
