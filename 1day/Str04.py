# Str04.py


a = '   Hello'
b = 'Hello   '
c = '  Hello  ' 

print(a.lstrip())
print(b.rstrip())
print(c.strip())


d = 'Hello안녕12'
e = 'Hello안녕'
print(d.isalpha())
print(e.isalpha())
print(d.isalpha() or d.isalnum())

f = 'Hello 안녕12'
print(f.isalnum())

x = 'Java, C, SQL, Python'
y = x.split(',')
z = ','.join(y)
print(y)
print(z)

k = 'Java   C  SQL    Python'
m = ','.join(k.split())
print(m)
