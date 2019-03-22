# Set03.py

# add(),update(),remove()

a = {10,20,30}
# print(a[1])

a.add(40)
print(a)
a.add(50)
print(a)
a.add(40)
print(a)

a.update({60,70})
print(a)

a.update({80})
print(a)

a.update([11,22])
print(a)

a.update((111,222))
print(a)

a.update((4444,))
print(a)

#a.update((777))
#print(a)

a.update(('AA',True))
print(a)

a.remove(4444)
print(a)

a.discard(222)
print(a)

#a.remove({'AA', True, 70, 40, 10})
#print(a)

a = a - {'AA', True, 70, 40, 10}
print(a)


























