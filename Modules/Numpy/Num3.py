import numpy as np

a = np.random.randint(1,100,(3,3))
print(a)
print()
x = a
print(x.sum(axis=0))
print()
print(a[(a > 10) & (a < 50)])
print()

b = np.random.rand(3,3)
print(b*10)