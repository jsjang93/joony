# for06.py




for i in range(0,11):
    print("{}".format(i), end=' ')

print()
print("="*30)


# 짝수만 출력
for i in range(0,11):
    if(i>7) : break       # break는 뒤로 탈출
    if(i%2)==1: continue  # continue는 앞으로 탈출
    print(i, end=' ')


for j in range(11): pass # pass는 일단 패스함 - 스켈레톤 디자인




