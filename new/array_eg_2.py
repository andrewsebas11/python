import numpy as np

# a = [[1, 14, 16], [18,20,22], [17, 19, 20]]
# o=[]
# print(len(a))
# print(a)
# for i in range(len(a)):
#     tmp=[]
#     for j in range(len(a[i])):
#         tmp.append((a[i][j])+2)
#     o.append(tmp)
# print(o)
#
# a1 = np.array(a)
# print(a1+2)

# arr1 = np.array([10, 25, 50, 75, 100, 125, 150, 200, 250])
# print(arr1)
#
# #slicing with start and stop values
# print(arr1[1:5])
# print(arr1[2:7])
# print(arr1[4:8])
# print(arr1[3:9])
#
# #slicing from first and last numbers
# print(arr1[3:])
# print(arr1[:7])

arr1 = np.array([10, 50, 100, 150, 250])

arr2 = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
                 [111, 194, 7, 22, 124], [82, 119, 18, 156, 81],
                 [38, 10, 151, 24, 14]])

arr3 = np.array([[12, 11, 0, 9, 7], [10, 4, 11, 6, 9],
                 [9, 2, 10, 9, 11], [5, 14, 0, 11, 8]])

print("Array 1.      : ", arr1)
print("Array 1 Shape : ", arr1.shape)

print("Array 2       : \n", arr2)
print("Array 2 Shape : ", arr2.shape)

print("Array 3       : \n", arr3)
print("Array 3 Shape : ", arr3.shape)

arr = np.random.randint(0, 5, size = 10)
print('Original Array = ', arr)

uniq = np.unique(arr)
print('Unique Items in arr = ', uniq)

arr2 = np.random.randint(10, 100, size = (3, 5))
print('\n---Two Dimensional Random Original Array----\n', arr2)

print(arr2)

uniq2 = np.unique(arr2)
print('Unique Items in arr2 = ', uniq2)


arr3 = np.random.randint(15, 25, size = (2, 3, 8))
print('\n----Three Dimensional Random Original Array----\n', arr3)

uniq3 = np.unique(arr3)
print('Unique Items in arr3 = ', uniq3)

arr = np.random.randint(0, 5, size = 10)
print('Original Array = ', arr)

uniq, cnt = np.unique(arr, return_counts = True)
print('Unique Items in arr = ', uniq)
print('Count Items in arr = ', cnt)

arr2 = np.random.randint(10, 100, size = (3, 5))
print('\n---Two Dimensional Random Original Array----\n', arr2)


uniq2, cnt2 = np.unique(arr2, return_counts = True)
print('Unique Items in arr2 = ', uniq2)
print('Count Items in arr2 = ', cnt2)


arr3 = np.random.randint(15, 25, size = (2, 3, 8))
print('\n----Three Dimensional Random Original Array----\n', arr3)

uniq3, cnt3 = np.unique(arr3, return_counts = True)
print('Unique Items in arr3 = ', uniq3)
print('Count Items in arr3 = ', cnt3)



