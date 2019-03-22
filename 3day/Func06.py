#Func06.py


a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}


def pDict(**d): # dictionary는 k, v --> 별 두개
    for i in d.items(): print(i)



pDict(**a)
pDict(사과='apple', 포도='grape', 바나나='banana')
pDict(**{'컵':'cup', '물':'water'})



