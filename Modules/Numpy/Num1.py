import numpy as np

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(a[0:1])
print(a[1:2])
print(a[2:3])

print(a[:,0:1])
print(a[:,1:2])
print(a[:,2:])

print(a[0][0],a[0][1])
print(a[1][0],a[1][1])

print(a[a>50])
print(a+100)