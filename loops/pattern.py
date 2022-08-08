n = 6
for i in range(n):
    for j in range(n+1):
        if (j == 0 or j == n) or (i == 0 and j != 0 and j != n) or (i == n - 1) or (i == n // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    for j in range(n+3):
        if ((i == 0) or (i == n-i)) and ((j > 0) or (j == 0) and (i != 0) and (i != n-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()