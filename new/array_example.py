import numpy as np
l = [1, 2, 3, 4, 5]
print(type(l))
print(l)
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l1)
print(type(l1))
l2 = [[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]], [[19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]]
print(l2)
print(type(l2))
a = np.array(l)
print((type(a)))
print(a)
b = np.array(l1)
print(type(b))
print(b)
c = np.array(l2)
print(type(c))
print(c)