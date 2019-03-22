# for12_Quiz.py

# Quiz 1) a 에서 abc 가 아닌 문자는 무엇인가요? (중복제거)
a = 'aybxczbcyazcaxbc'
b = { s for s in a if s not in 'abc' }
print(b)



# Quiz 2) 학생들의 국어점수가 70 이상이면 '합격', 아니면 '불합격'
국어점수 = {'Tom':90,'Jane':60,'Alice':70}
print(국어점수)
r = {k:a for k,v in 국어점수.items() if v >= 70 a = '합격' elif a = '불합격'}
# 결과 ==> {'Tom': '합격', 'Jane': '불합격', 'Alice': '합격'}



# Quiz 3 ) 수학 점수가 0이 아닌 학생들만 출력하세요
#          단, 70이상은 합격, 미만은 불합격 표시
수학점수 = {'Tom':90,'Jane':60,'Alice':0,'Hong':78,'Kim':45}
z = {}
print(z)
# 결과 ==> {'Tom':'합격','Jane':'불합격,'Hong':'합격','Kim':'불합격}














