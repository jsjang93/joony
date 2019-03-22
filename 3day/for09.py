# for09.py


a = []

# a 에 for문을 사용해서 1 ~ 10 까지 입력

# a[0] <- 1, a[9] <- 10


for i in range(0,10,1):
    #a[i] = i+1        <----- 얘만 error
    #a = a + [i+1]  
    #a.append(i+1)

    # append: 원래 있던거에 element 추가
    # extend: 원래 있던거에 list 추가
    

print(a)
