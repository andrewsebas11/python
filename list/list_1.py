l = []
print(type(l))
print(l)
l1 = [1, 2, 3, 4, 5, 6, 7]
print(l1)
print(l1[0])
print(l1[2])
print(l1[4])
print(l1[-1])
print(l1[-3])
print('-------------------------------')
l2 = [9, 7, 1, -4, 99, 87]
print(l2)
print(sum(l2))
print(max(l2))
print(min(l2))
print(len(l2))
print('-------------------------------')
#slicing
l3 = [1, 2, 4, 9, 81, 87, 19, 20]
print(l3)
print(l3[:])
print(l3[2:])
print(l3[:4])
print(l3[2:6])
print(l3[2:-3])

print('-------------------------------')

l4 = []
print(l4)
l4.append(8)
l4.append(81)
l4.append(71)
print(l4)
l4.insert(0, 111)
l4.insert(1, 121)
l5 = [1, 2, 3]
l4.extend(l5)
print(l4)
l4.pop()
print(l4)
l4.pop()
print(l4)
l4.remove(8)
print(l4)
l4.sort()
print(l4)
l4.sort(reverse=True)
print(l4)

a = 'abcdefgh' [::-1]
print(a)

s = 'mam'
s1 = 'mom'
s2 = 'cat'
s3 = s[::-1]
s4 = s1[::-1]
s5 = s2[::-1]
if s == s3:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
if s1 == s4:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
if s2 == s5:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


