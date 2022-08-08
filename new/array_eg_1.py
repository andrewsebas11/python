import numpy as np
a = [1, 2, 3, 4, 5]
o = []
for b in range(len(a)):
    o.append(a[b]+2)
print(o)
a1 = np.array(a)
print(a1+2)
print(a1*2)

a=np.arange(5)
print(a)
print(np.arange(10))
print(np.arange(15))


print(np.linspace(0, 1, 3))
# print(np.linspace(1, -1, 7))


# print(np.zeros((2, 2)))
# print(np.zeros((4, 7)))
# print(np.ones((3, 4, 7)))


print(np.full((3, 4), 9))

print(np.empty((2, 3)))

print(np.eye(2))