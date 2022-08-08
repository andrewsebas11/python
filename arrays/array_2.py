import re
import numpy as np
# str = 'I welcome all to besant and all welcome'
# print(str)
# a = re.split(' ', str)
# print(a)
# arr = np.array(a)
# print(arr)
# uniq, count = np.unique(arr, return_counts=True)
# print(uniq)
# print(count)


print('Printing Original array')

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print(sampleArray)


print('Array after deleting column 2 on axis 1')

sampleArray = np.delete(sampleArray, 1, axis=1)

print(sampleArray)

arr = np.array([[10, 10, 10]])


print('Array after inserting column 2 on axis 1')

sampleArray = np.insert(sampleArray, 1, arr, axis=1)

print(sampleArray)