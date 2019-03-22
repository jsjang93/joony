# Try01.py
# try except els finally




print('숫자 입력')
x = input()

try:
    print(10/int(x))
except ZeroDivisionError as e: # 예외처리
    print('0은 안돼요~')
    print(e)
except ValueError as v:
    print('숫자만 넣어주세요~')
    print(v)
else: # 성공시 출력
    print('좋은 입력이어따..')
finally:  # 항상 출력되는 문
    print('End of Document')
