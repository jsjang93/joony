# Str03.py




a = '20190311Mon'

date = a[:8]
day = a[8:]

print(date, day)


# 일시 : ~~~~~
# 요일 : ~~~~~

print("일시 : " + date)
print("일시 : {0}".format(date))
print("일시 ; {}".format(date))
print("{0} {1} {2}".format('일시', ":", date))
print("{1} {0} {2}".format(':', "일시", date))
print("{} {} {}".format('일시', ":", date))

b = 'Pithon'
b_s = b.split('i')
b_r = b.replace('i', 'y')
print(b_s[0] + "y" + b_s[1])
print(b_r)













