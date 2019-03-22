# List03.py

a = [65,12,98,43,35]
a.sort()
print(a)

b = [65,12,98,43,35]
b.reverse()
print(b)

c = [65,12,98,43,35]
# 98,65,43,35,12
c.sort(); c.reverse()
print(c)

d = [65,12,98,43,35]
d.sort(reverse =True)
print(d)

e = [65,12,98,43,35]
f = sorted(e)
print(e, f)

##############################
print("========================================")
##############################

g1 = 100; g2 = 100
g3 = g4 = g5 = 100
print(g1,g2,g3,g4,g5)
print(id(g1),id(g2),id(g3),id(g4),id(g5))

h1 = [65,12,98,43,35]
h2 = [65,12,98,43,35]
h3 = h1 # h3는 h1의 다른이름일 뿐

print(id(h1),id(h2),id(h3))

h1[1] = 120
print(h1[1],h3[1],h2[1])

print(h1[:])

h4 = h1[:] # 복사!
print(id(h1),id(h2),id(h3),id(h4))

#######################################
print("========================================")
#######################################

print(g1,g2)

g1 = None
print(g1)

del g1
#print(g1)

x = [1,2,3]
y = [4,5,6]
print(id(x), id(y))

z = x + y
x.extend(y)
print(id(x), id(y))
print(id(z))
print(x)






























































