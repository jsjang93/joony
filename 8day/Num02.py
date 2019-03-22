# Num02.py
import numpy as np
d1 = list(range(1,13))
print(d1) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a1 = np.array(d1).reshape(3,2,2)
print(a1.shape,a1.ndim)
print(a1)

a2 = np.array(list(range(1,7))).reshape(2,3)
print(a2.shape,a2.ndim)
print(a2)

a3 = np.zeros(6).reshape(2,3)
print(a3)

a4 = np.ones(9); print(a4)
a5 = np.eye(5); print(a5)

a6 = np.arange(1,13).reshape(2,6); print(a6)

a7 = np.random.randn(1,3); print(a7)

a8 = np.array([1,2,3,4,5],dtype=np.float64)
print(a8,a8.dtype)

a9 = np.array([1,2,3,4,5],dtype=np.int64)
print(a9,a9.dtype)

a10 = np.array(list(range(1,7))).reshape(2,3)
print(a10,a10.dtype)
a11 = a10.astype(np.float64)
print(a11,a11.dtype)

a12 = a11.astype(np.str) # <-- str
print(a12,a12.dtype)

a13 = a11.astype(np.string_) # <-- str
print(a13,a13.dtype)

