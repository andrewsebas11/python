# for a in range(0, 7):
#     if a == 3:
#         for b in range(0,4):
#             print('M', end=" ")
#     else:
#         for b in range(0, 4):
#             if b == 0 or b == 3:
#                 print('A', end=" ")
#             else:
#                 print(' ', end=" ")
#     print()

# for a in range(0, 7):
#     if a == 3:
#         for b in range(0,4):
#             print('*', end=" ")
#     else:
#         for b in range(0, 4):
#             if b == 0 or b == 3:
#                 print('*', end=" ")
#             else:
#                 print(' ', end=" ")
#     print()

for a in range(0,4):
    if a == 2:
     for b in range(0, 4):
        print('*', end=" ")
    elif a == 1 or a==3:
        for b in range(0, 4):
            if b == 0 or b == 3:
                print('*',end =" ")
            else:
                print(' ', end=" ")
    else:
        for b in range(0, 4):
            if b == 1:
                print(" * ",end=" ")
            else:
                print(" ", end=" ")
    print()



