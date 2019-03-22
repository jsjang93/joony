# Quiz01.py
    
Items = {"콜라":1000,"사이다":900,"씨그램":500,"우유":700,"활명수":800}

print("=== 음료 자판기 입니다 ====")
print("[콜라][사이다][씨그램][우유][활명수] 중 선택")
print("복수 선택 시 --> 예) 사이다,우유 ")

tem = input().strip().split(',')
print(tem)

def calc(*s):
    money = 0
    for i in s:
        money += Items[i]        
    return money



print("가격: " + str(calc(*tem)) +"원")

# 가격: 1600 원









