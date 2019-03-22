# Test09.py - bool -> True, False ; and, or, not, if, for, while

print(True and False)
print(True or False)
print(True & False)
print(True | False)

print(0 and 3)
print(3 and 6)
print(6 & 3)
print(3 or 6) # 3
print(6 or 3) # 6
print(6 or 0) # 6
print(0 or 6) # 6
print(6 | 3)
# 논리연산, 비트논리연산

print(bool(0), bool(0.00)) # False
print(bool(None)) # False
print(bool('')) # False
print(bool([]), bool({}), bool()) # False, F, F
# False : 0, '', [], (), {}, None, False, not True
#  if not []:  --> data 긁어왔는데 그 데이터가 있으면,

print(True, not True)
print(not 1)
print(not -1)
print(not 0.1)
print(not 0)
print(int(not not -2)) # 1; True -> int로 형변환
# 숫자에서 0을 제외한 모든 값이 True이다. --> bit로 생각

print(~~0)
print(~0)
print(~1)
# ~(틸드)는 비트 반전

