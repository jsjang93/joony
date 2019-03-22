# for08.py

nd1 = [[10,20,30],
       [40,50,60],
       [70,80,90]]
'''
10 20 30 
40 50 60 
70 80 90
'''

for i in range(0,3):
    for j in range(0,3):
        print(nd1[i][j], end=' ')
    print()
        


print("###############################")

nd2 = [[10,20,30,40],
       [40,50],
       [70,80,90]]

for i in range(0,len(nd2)):
    for j in range(0,len(nd2[i])):
        print(nd2[i][j], end=' ')
    print()
        



'''
10 20 30 40 
40 50 
70 80 90
'''




