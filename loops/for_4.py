for a in range(1, 10):
    if a%2 == 0:
        print("even")
    else:
        print("odd")
for b in range(1, 11):
    if b%2 == 0:
        print(f"the {b} is even")
    else:
        print(f"the {b} is odd")

z = 65
print(chr(z))
print(chr(66))

c = 1
for a in range(1, 6):
    for b in range(1, a+1):
        if c%2 == 0:
            print(f"{c}even", end=" ")
        else:
            print(f"{c}odd", end=" ")
        c += 1
    print()

n = 5
z = 65
for a in range(0,6):
    for b in range(0,a+1):
        print(chr(z), end=" ")
    z+=1
    print()

z = 65
for a in range(0,6):
    for b in range(0,a+1):
        print(chr(z), end=" ")
        z+=1
    print()

c=1
for a in range(0, 6):
    for b in range(0, a+1):
        if a%2 == 1:
            print(c, end=" ")
            c+=1
        else:
            print('*', end=" ")
            c+=1
    print()



