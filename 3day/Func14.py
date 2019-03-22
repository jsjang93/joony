# Func14.py - anonymous fcn



nocall = ['바보', '멍청이', '오영택']

def Hi(name='손'):
    if name in nocall : return
    print('{}님, 안녕하세요'.format(name))

Hi() # 손님, 안녕하세요
Hi('홍길동') # 홍길동님, 안녕하세요
Hi('바보') #

