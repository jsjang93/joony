# Re01.py
import re
a1 = 'pizza'; a2 = 'banana'; a3 = 'az'

r = re.compile("[az]")

print(r.search(a1))
print(r.search(a2))
print(r.search(a3)) #search는 a나z둘중 하나라도 걸려도 됨
