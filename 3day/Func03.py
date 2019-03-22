# Func03.py

# 숫자를 입력받아서 그 숫자만큼 * 를 출력하는 함수를 만드세요
def pStar1(count):
    print("*"*count)

    
pStar1(5) #==>  *****
pStar1(3) #==>  ***





# 숫자와 문양을 입력받아서 그 숫자만큼 문양을 출력하는 함수를 만드세요
def pStar2(num = 5, shape = "$"):
    print(shape*num)

 

pStar2(5,'*') #==>  *****
pStar2(3,'@') #==>  @@@
pStar2(4) #==> $$$$
pStar2()  #==> $$$$$






