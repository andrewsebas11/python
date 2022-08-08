# for i in range(10):
#     if i%2==0:
#         print(i)
# print('this is even numbers')

# for a in 'human':
#     print(a)
# for x in 'human':
#     print(x, end="")


# l = [9, 8, 10, 12]
# for a in range(len(l)):
#     print(l[a])
#     print(l[a]*10)
#
# for a in range(1, 15):
#     print(f"{a} * {19} = {a*19}")
#
# n = int(input("enter the number of rows to print"))
# t = int(input("enter the first number"))
# for a in range(1, n+1):
#     print(f"{a} * {t} = {a*t}")
#     print(f"{a} * {t} = {a * t}", end=" ")


for a in range(1, 6):
    for b in range(1, 6):
        print(a, end=" ")
    print()
print('------------------')
for a in range(1, 6):
    for b in range(1, 6):
        print(b, end=" ")
    print()
print('------------------')
for a in range(1, 6):
    for b in range(1, 6):
        print(a*b, end=" ")
    print()
print('------------------')
for a in range(1, 11):
    for b in range(1, 11):
        print(f"{a} * {b} = {a*b}", end=" ")
    print()
print('------------------')
for a in range(1, 6):
    for b in range(1, a+1):
        print(a, end=" ")
    print()
print('------------------')
# c = 1
# for a in range(1, 6):
#     for b in range(1, a+1):
#         print(c, end=" ")
#         c ** 2
#     print()
# print('------------------')
for a in range(1, 6):
    for b in range(1, a+1):
        print(a*b, end=" ")
    print()
print('------------------')
c = 1
for a in range(1, 6):
    for b in range(1, a+1):
        print(c*c, end=" ")
        c += 1
    print()
print('------------------')