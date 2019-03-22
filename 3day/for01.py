# for01.py


iArr = (10,20,30)
for i in iArr:
    print(i)



sArr = ['사과','배','바나나']
for s in sArr:
    print(s)



z = 'HPEducation'
for s in z:
    print(s)



a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}

for k in a.keys():
    print(k)

for v in a.values():
    print(v)

for i,j in a.items():
    print(i,j)

for z in a.items():
    print(z)


find_tem = input("뭐가 궁금해\n")
for i,j in enumerate(a.keys()):
    if j==find_tem:
        print("{}는 {}번째에 있다.".format(j, i+1))
        break



