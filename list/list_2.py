# l = []
# for a in range(1, 100):
#     if a % 2 == 0:
#         l.append('even')
#     else:
#         l.append('odd')
#     print(l)
# print('-----------------------')
# pl = []
# nl = []
# for a in range(1, 6):
#     n = int(input(f"enter the number {a}"))
#     if n < 0:
#         nl.append(n)
#     else:
#         pl.append(n)
# print(pl)
# print(nl)
# print(max(pl))
# print(min(pl))
# print(sum(pl))
# print(len(pl))
# print(max(nl))
# print(min(nl))
# print(sum(nl))
# print(len(nl))
#
# l1 = []
# print(dir(l1))
#
# n1 = [1, 2, 3]
# print(n1)
# n1.clear()
# print(n1)
#
# n2 = [1, 2, 3, 4]
# n3 = n2.copy()
# print(n2)
# print(n3)
# print(n2 == n3)
# l = [1, 2, 4, 6, 12, 14, 16, 22]
# largest_number = l[0]
# second_largest_number = l[0]
# third_largest_number = l[0]
# for i in l:
#     if i > largest_number:
#         third_largest_number = second_largest_number
#         second_largest_number = largest_number
#         largest_number = i
#     elif i > second_largest_number:
#         third_largest_number = second_largest_number
#         second_largest_number = i
#     elif i > third_largest_number:
#         third_largest_number = i
# print(f"the third largest number is {third_largest_number}")
# l.sort(reverse=True)
# print(l[2])
s = ['dog1', 'cat123', 'a', 'ab']
o = s.index(max(s, key=len))
print(o)

